from pyrbs import CanMessage, PyRbs, Timer


rbs = PyRbs()

control_01_msg: CanMessage = rbs.can_message.get("CAN2.Control_01")
timer_1s: Timer = rbs.timer.add(
    "timer_1s",
    1.0,
    active_on_start=True,
)


@rbs.timer.on("timer_1s")
def on_timer_1s(_timer: Timer):
    control_01_msg.send()


@rbs.can_message.on("CAN2.Control_01")
def on_control_01_msg(message: CanMessage):
    print(f"Activate status: {message['Activate'].raw}")
