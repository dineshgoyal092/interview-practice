from controllers.topicController import TopicController
from controllers.producerController import ProducerController
from controllers.consumerController import ConsumerController
from services.consumerService import ConsumerService
from services.producerService import ProducerService
from services.topicService import TopicService
from services.customThreadService import CustomThreadService
from models.message import Message

topicController = TopicController(TopicService())
producerController = ProducerController(ProducerService())
consumerController = ConsumerController(ConsumerService(), CustomThreadService(), TopicService())

import time
with open("input.txt", 'r') as f:
    f.readline()
    for line in f:
        input = line.split()
        # print(input)
        command = str(input[0])
        if command == "addTopic":
            topicName = str(input[1])
            topicController.addTopic(topicName)
            print("topic Added", topicName)
        elif command == "addProducer":
            producerName = str(input[1])
            producerController.addProducer(producerName)
            print("producer Added", topicName)
        elif command == "addConsumer":
            consumerName = str(input[1])
            consumerController.addConsumer(consumerName)
            print("consumer Added", topicName)
        elif command == "subscribe":
            consumerName = str(input[1])
            topicName = str(input[2])
            consumerController.subscribeToTopic(consumerName, topicName)
            print("subscribed", consumerName, topicName)
        elif command == "publish":
            producerName = str(input[1])
            topicName = str(input[2])
            text = str(input[3])
            message = Message(text, producerName)
            topicController.addMessage(topicName, message)
            print("message published", topicName, text)
            time.sleep(3)
        elif command == "unSubscribe":
            consumerName = str(input[1])
            topicName = str(input[2])
            print("unSubscribed", consumerName, topicName)
            consumerController.unSubscribeToTopic(consumerName, topicName)
            print("unSubscribedSuccess", consumerName, topicName)
            time.sleep(5)