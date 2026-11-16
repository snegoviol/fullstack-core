# ==================================================================================================
# 
# Copyright (c) 2026 Ilya Snegov
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Originally from Human Pose Estimation Service 
# (https://github.com/snegoviol/pose-estimation-service).
# Modified for Full-Stack Core to suit the needs of this project.
# 
# ==================================================================================================
# packages/shared/src/celery_lib/instance.py
# ==================================================================================================

from kombu import Exchange, Queue
from celery import Celery
from celery.schedules import crontab
from redis_lib import redis_config
from .config import celery_config

# ==================================================================================================

tasks_exchange = Exchange(
    celery_config.exchange_name,
    type=celery_config._exchange_type,
)
"""
Celery exchange used to route tasks to their respective queues.
"""

# ==================================================================================================

inference_queue = Queue(
    celery_config.queue_name_inference,
    exchange=tasks_exchange,
    routing_key=celery_config.queue_name_inference,
)
"""
Queue for AI inference tasks, routed via the shared exchange.
"""

# ==================================================================================================

maintenance_queue = Queue(
    celery_config.queue_name_maintenance,
    exchange=tasks_exchange,
    routing_key=celery_config.queue_name_maintenance,
)
"""
Queue for maintenance and scheduled tasks, routed via the shared exchange.
"""

# ==================================================================================================

celery_app = Celery(
    celery_config.app_name,
    broker=redis_config.broker_url,
    backend=redis_config.result_backend_url,
)
"""
Celery application instance configured with Redis as both message broker and result backend.
"""

# ==================================================================================================

celery_app.conf.update(
    task_serializer=celery_config._task_serializer,
    result_serializer=celery_config._result_serializer,
    accept_content=celery_config._accept_content,
    timezone=celery_config._timezone,
    enable_utc=celery_config._enable_utc,
    result_expires=celery_config.result_expires,
    task_queues=(inference_queue, maintenance_queue),
    beat_schedule={
        celery_config.schedule_name_reset_inference_counts: {
            "task": celery_config.task_name_reset_inference_counts,
            "schedule": crontab(
                hour=celery_config.hour_reset_inference_counts,
                minute=celery_config.minute_reset_inference_counts,
            ),
            "options": {
                "queue": celery_config.queue_name_maintenance,
            },
        },
    },
)
"""
Celery application configuration: serialization policies, timezone settings, task routing, and periodic schedules.
"""

# ==================================================================================================
