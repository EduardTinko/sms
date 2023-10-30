1. Install deps:

```
pip install -r requirements.txt
```

2. Run broker:

```
docker run -d -p 5672:5672 rabbitmq
```

3. Set you TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN in environment variables:

Linux, macOS
```
export TWILIO_ACCOUNT_SID='foo'
export TWILIO_AUTH_TOKEN='foo'
```
Windows
```
setx TWILIO_ACCOUNT_SID 'foo'
setx TWILIO_AUTH_TOKEN 'foo'
```

4. Run worker process:

Linux, macOS
```
celery -A site_sms worker -l INFO
```
Windows
```
celery -A site_sms worker -l INFO -P eventlet
```

5. Run Django web server
```
python manage.py runserver
```