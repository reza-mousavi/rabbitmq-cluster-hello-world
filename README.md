# RabbitMQ Clustering Hello World

The project is created to practice RabbitMQ clustering

Project consist of two setups
- Classic clustering, where cluster configuration is achieved via config files only
- Consul, where nodes register themselves and find peers through Consul 

# Running Application

It is required to have **docker** and **docker compose** installed. Both setups come with
a simple producer created on Python which are built a s part of docker-compose start up

## Classic Clustering

Switch to classic folder and run the following statement on the terminal:

```
> docker-compose up -d
```

### RabbitMQ Management Console

After successful startup, RabbitMQ management console could be reached out at http://localghost:15672

## Clustering Using Consul

Switch to **consul** folder and run the following statement on the terminal:

```
> docker-compose up -d
```

### RabbitMQ Management Console

After successful startup, **RabbitMQ Management** console could be reached out at http://localhost:15672

### Consul UI

After successful startup, **Consul** UI could be reached out at http://localhost:8500/

# Useful links

| Tool                | Version                                  |
|---------------------|------------------------------------------|
| Python              | https://www.python.org/                  |
| Docker              | https://www.docker.com/                  |
| RabbitMQ Clustering | https://www.rabbitmq.com/docs/clustering |


