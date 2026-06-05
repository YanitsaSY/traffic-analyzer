import redis
import time
import random
import json

# Свързваме се с контейнера на базата данни чрез DNS името 'redis_db'
r = redis.Redis(host='redis_db', port=6379, decode_responses=True)

countries = ['Bulgaria', 'USA', 'Germany', 'Japan', 'UK', 'Brazil']
browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
endpoints = ['/home', '/products', '/cart', '/checkout', '/api/v1/user']

print("🚀 Генераторът на трафик стартира...")

while True:
    visit_data = {
        "timestamp": time.time(),
        "country": random.choice(countries),
        "browser": random.choice(browsers),
        "page": random.choice(endpoints),
        "status_code": random.choice([200, 200, 200, 404, 500])
    }
    
    # Записваме данните в Redis в списък 'site_traffic'
    r.lpush('site_traffic', json.dumps(visit_data))
    r.ltrim('site_traffic', 0, 99) # Пазим само последните 100 записа
    
    print(f"📥 Посещение от {visit_data['country']} на {visit_data['page']} ({visit_data['status_code']})")
    time.sleep(2)