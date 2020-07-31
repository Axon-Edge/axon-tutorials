import time
import axon

# INSERT YOUR AXON WRITE KEY HERE
# axon.write_key = '<PASTE_WRITE_KEY_HERE>'

def upload_mock_events():
    mock_data = [78.5, 78.8, 79.0, 79.0, 79.2]
    for temp_value in mock_data:
        # Axon Track Command
        axon.track(tracking_type="temperature", data=temp_value)
        time.sleep(1)

upload_mock_events()
