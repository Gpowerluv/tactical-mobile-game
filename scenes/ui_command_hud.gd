extends Control

class_name UICommandHUD

signal order_selected(order_type)

var available_orders = ["MOVE", "ATTACK", "BOUNDING_OVERWATCH", "REGROUP"]
var is_radial_open = false

func _ready() -> void:
	# Initialize command HUD state
	set_process_input(true)

func _input(event: InputEvent) -> void:
	# Example input toggle for mobile touch or key press
	if event.is_action_pressed("ui_accept"):
		toggle_radial_menu()

func toggle_radial_menu() -> void:
	is_radial_open = !is_radial_open
	if is_radial_open:
		trigger_radial_menu()
	else:
		close_radial_menu()

func trigger_radial_menu() -> void:
	print("Displaying tactical command radial menu...")
	for order in available_orders:
		print("Available option: ", order)

func close_radial_menu() -> void:
	print("Radial menu closed.")

func select_order(order_index: int) -> void:
	if order_index >= 0 and order_index < available_orders.size():
		var chosen_order = available_orders[order_index]
		emit_signal("order_selected", chosen_order)
		print("Order issued: ", chosen_order)
		close_radial_menu()
