from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def get_mic_interface():
    devices = AudioUtilities.GetMicrophone()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    )
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume


def mute_microphone(speaker):
    try:
        volume = get_mic_interface()
        volume.SetMute(1, None)

        speaker.say("Microphone muted")

    except Exception as e:
        print("Mic mute error:", e)
        speaker.say("Could not mute microphone")

    speaker.runAndWait()

#  wont work as in the state of muted, the assistant wont get the command (haha)
def unmute_microphone(speaker):
    try:
        volume = get_mic_interface()
        volume.SetMute(0, None)

        speaker.say("Microphone unmuted")

    except Exception as e:
        print("Mic unmute error:", e)
        speaker.say("Could not unmute microphone")

    speaker.runAndWait()
