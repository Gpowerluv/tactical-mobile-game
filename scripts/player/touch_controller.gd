extends Node3D
class_name TacticalTouchController

# Sensitivity settings tailored for mobile touchscreens
@export var look_sensitivity: float = 0.005
@export var camera_node: Camera3D
@export var player_node: CharacterBody3D

var look_touch_index: int = -1
var last_touch_pos: Vector2 = Vector2.ZERO

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventScreenTouch:
		# Detect right side of screen for camera look drag
		if event.position.x > get_viewport().get_visible_rect().size.x / 2:
			if event.pressed:
				look_touch_index = event.index
				last_touch_pos = event.position
			elif event.index == look_touch_index:
				look_touch_index = -1

	elif event is InputEventScreenDrag:
		# Process camera rotation on drag
		if event.index == look_touch_index and camera_node and player_node:
			var delta_touch = event.position - last_touch_pos
			last_touch_pos = event.position
			
			# Rotate character horizontally (Y-axis)
			player_node.rotate_y(-delta_touch.x * look_sensitivity)
			
			# Rotate camera vertically (X-axis) with pitch clamping
			camera_node.rotate_x(-delta_touch.y * look_sensitivity)
			camera_node.rotation.x = clamp(camera_node.rotation.x, deg_to_rad(-80), deg_to_rad(80))
