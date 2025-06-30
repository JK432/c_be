from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
import joblib
from django.conf import settings
import os

MODEL_PATH = os.path.join(settings.BASE_DIR, 'api', 'ml_models', 'bot_detector_xgb.pkl')
model = joblib.load(MODEL_PATH)


def extract_features(data):
    mouse = data["mouse_movements"]
    clicks = data["click_patterns"]
    typing = data["typing_patterns"]

    if len(mouse) >= 2:
        times = [m["time"] for m in mouse]
        xs = [m["x"] for m in mouse]
        ys = [m["y"] for m in mouse]

        duration = times[-1] - times[0]
        distances = [np.hypot(xs[i] - xs[i - 1], ys[i] - ys[i - 1]) for i in range(1, len(xs))]

        time_diffs = np.diff(times).astype(float)
        time_diffs[time_diffs == 0] = np.nan

        speeds = np.array(distances) / time_diffs
        speeds = speeds[np.isfinite(speeds)]

        if len(speeds) > 0:
            avg_speed = np.mean(speeds)
            max_speed = np.max(speeds)
        else:
            avg_speed = 0
            max_speed = 0

        total_distance = np.sum(distances)
    else:
        duration = 0
        total_distance = 0
        avg_speed = 0
        max_speed = 0

    return {
        "mouse_duration": duration,
        "mouse_distance": total_distance,
        "mouse_avg_speed": avg_speed,
        "mouse_max_speed": max_speed,
        "click_count": len(clicks),
        "typing_count": len(typing),
        "response_time": data["response_time"],
    }


class SessionClassificationViewSet(ViewSet):
    @action(detail=False, methods=['post'])
    def classify(self, request):
        new_session = request.data

        if not isinstance(new_session, list):
            return Response({"error": "Expected a list of session objects."}, status=status.HTTP_400_BAD_REQUEST)

        sample_features = [extract_features(d) for d in new_session]
        df_sample = pd.DataFrame(sample_features)
        pred = model.predict(df_sample)
        label_map = {0: "Bot", 1: "Human"}
        predictions = [label_map[p] for p in pred]

        return Response({"classification": predictions})