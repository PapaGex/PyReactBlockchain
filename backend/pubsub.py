import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-c23d907a-a890-11ec-8a23-de1bbb7835db'
pnconfig.publish_key = 'pub-c-28247e2b-a390-49a9-8c99-816245e91a8f'
# pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

class PubSub():
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(TEST_CHANNEL,{'Blood': 'Lines'})

if __name__ == '__main__':
    main()
