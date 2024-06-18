import os

directories = [d for d in os.listdir('src') if os.path.isdir(os.path.join('src', d))]

for dir in directories:
    with open(f'src/microservices.yaml', 'w') as f:
        f.write(f'''
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {dir}-service
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {dir}-service
  template:
    metadata:
      labels:
        app: {dir}-service
    spec:
      containers:
        - name: {dir}-service
          image: {dir}-service-image
          ports:
            - containerPort: 8080
''')
