from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-c23d907a-a890-11ec-8a23-de1bbb7835db'
pnconfig.publish_key = 'pub-c-28247e2b-a390-49a9-8c99-816245e91a8f'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming Message_Object: {message_object}')

pubnub.add_listener(Listener())

def main():
    pubnub.publish().channel(TEST_CHANNEL).message({ 'Blood': 'bar' }).sync()

if __name__ == '__main__':
    main()