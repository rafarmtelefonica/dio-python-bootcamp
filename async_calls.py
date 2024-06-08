from fastapi import FastAPI
from httpx import AsyncClient
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.client = AsyncClient()

@app.on_event("shutdown")
async def shutdown():
    await app.client.aclose()

@app.get("/make_requests")
async def make_requests():
    '''
    url = "https://api-hml.telefonica.com.br/oauth2/v1/tokens"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic OWZmNGQ0NzQ5MzRjNDdiZTg4ZDYyY2VmNzcwODkwYTc6YllHMlpxM3RCWDRTWlVQekVuSQ==",
        "app-key": "57eec1f7-1f45-4f26-a482-e046f8d1d9aa",
        "OAM": "MDA1"
    }
    data = {
        "grant_type":"password",
        "username":"SVC_FINTECH",
        "password":"Vivo@2023",
        "scope":"ServiceAccount.Profile"
    }
    tasks = []
    for _ in range(50):
        tasks.append(app.client.post(url, headers=headers, data=data))
    responses = await asyncio.gather(*tasks)
    return {"responses": [response.json() for response in responses]}
    '''

    url = "https://fintech-hml.vivo.com.br/gateway/auth/v1/personal/password"
    headers = {
        "Authorization": "Bearer eyJraWQiOiJWaXZvQ3VzdG9tZXJEb21haW4iLCJ4NXQiOiJjc3dYdHZ4SU51M3JBWTl0YmI1c1ZEcWJ6ZnMiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGhobWwudml2by5jb20uYnI6NDQzL29hdXRoMiIsImF1ZCI6IjE5NDI2Yzc0MDAyNzRlMjM5NGQ5NWNkMDAyNzY4NzdiIiwiZXhwIjoxNzE3NjI5OTgyLCJqdGkiOiJNSGVObXBxODhSb2pudGs4YWptb0hRIiwiaWF0IjoxNzE3NjI2MzgyLCJzdWIiOiI0MDQ5MzYzMDg5OSIsImNsaWVudCI6IjE5NDI2Yzc0MDAyNzRlMjM5NGQ5NWNkMDAyNzY4NzdiIiwic2NvcGUiOlsib3BlbmlkIiwiQ3VzdG9tZXIuUHJvZmlsZSJdLCJkb21haW4iOiJWaXZvQ3VzdG9tZXJEb21haW4iLCJlbnRyeVVVSUQiOiJmYTk1MGExNC1kYmRiLTQzZDgtODQxNi05ZmNkMzAyOTBiZTkiLCJ2aXZvLmVuZHBvaW50IjoiVml2b0N1c3RvbWVyRG9tYWluIiwibnJkb2N1bWVudG8iOiI0MDQ5MzYzMDg5OSIsInZpdm8uZW52IjoiUFJFLVBST0QxMiJ9.IYJ3SMNWZ3StvmHrSrXQL43V0V_KdG5SKoDdaDETEwDg41xVZxzt810D51egJzldbuPYIDJJp8IKzKdT6JPY3-6z1gcl62-KR2OtOUb5yYP5JbIrQJX5Gv-T1xfk4lnTQEtlVip24Hv4YaQsE-sTuKHdcvw194q0a6a9dBCuS4Vf3R0c5vbOayWEnpNqFqpm6SQVUAy8erUL8SzKvw5ulbpyjL5TghMRN-OidzsB4QNQ3sV3EOJHuNbU71zP6Z9XiooHGloD0HrxGMU97FwQpIz_Y3uye2kHpuABUlzaA4bskDHIVnCPrLZlFFE7cTGlGJTlPtcFZWwGhWR0Jk6dvg",
    }
    data = {
        "password": "135791",
        "type": "TRANSACTION_PASSWORD"
    }
    tasks = []
    for _ in range(5):
        tasks.append(app.client.post(url, headers=headers, json=data))
    responses = await asyncio.gather(*tasks)
    return {"responses": [response.json() for response in responses]}

# pip install fastapi httpx
# python3 -m uvicorn async_calls:app --reload

''''
delete from tb_password where customer_id = '40493630899'
select * from tb_password where customer_id = '40493630899'
'''