from pyrbs import CanMessage, CanSignal, PyRbs, Timer


rbs = PyRbs()

control_01_tx: CanMessage = rbs.can_message.get("CAN1.Control_01")
target_speed_tx: CanSignal = rbs.can_signal.get("CAN1.Control_01.Target_Speed")
target_speed_tx.phys = 0.0

timer_1s: Timer = rbs.timer.add(
    "signal_timer_1s",
    1.0,
    active_on_start=True,
)


@rbs.timer.on("signal_timer_1s")
def send_next_target_speed(_timer: Timer):
    next_speed = target_speed_tx.phys + 250.0
    target_speed_tx.phys = 0.0 if next_speed > 4000.0 else next_speed
    control_01_tx.send()


@rbs.can_message.on("CAN2.Control_01")
def on_control_01_received(message: CanMessage):
    received_target_speed: CanSignal = message["Target_Speed"]
    print(f"CAN2 Target_Speed: {received_target_speed.phys:.0f} rpm")
