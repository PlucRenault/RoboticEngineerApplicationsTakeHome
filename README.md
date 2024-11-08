# Vention Robotic Engineer – Applications Take-home Test

## Introduction

This test is design to analyse the knowledge level of Robotic Engineer applicant.

---
# 1. Design 

## Question 1: What cobot would be best fitted for the client?
1. Doosan M1013
2. Doosan H2515
3. UR3e
4. UR10e
5. CRX 10iA

### Answer:
For this application, the FANUC CRX 10iA would be the best-suited collaborative robot (cobot) if the workpieces are consistently centered on the tables. Here’s why it would be the optimal choice:

1.	Adequate Payload Capacity: The CRX 10iA has a maximum payload of 10 kg, which comfortably accommodates the 7 kg cardboard box and 0.5 kg wooden cube. This capacity ensures that the cobot can handle the weight requirements without straining or sacrificing precision.

2. Sufficient Reach for Centered Workpieces: The CRX 10iA has a reach of 1.2 meters, which is sufficient for moving workpieces between tables, provided the boxes are placed in the center. This allows it to complete the pick-and-place tasks without needing additional reach, reducing unnecessary costs associated with larger models.

3. Ease of Use and Programming: FANUC’s CRX series is known for its user-friendly, tablet-based programming interface, which simplifies operation, especially for non-experts. The drag-and-drop style programming can reduce training time and help operators quickly adapt the robot to new tasks, aligning with the client's goal for a repurposable system.

4. Cost-Effectiveness Compared to H2515: Although the Doosan H2515 offers a greater reach (1.5 meters) and higher payload (25 kg), it is more expensive and may be overpowered for this task if the boxes are centered. The CRX 10iA meets the functional requirements at a lower cost, making it a more economical choice if the workpieces’ positioning doesn’t require extended reach.

Conclusion:
If workpieces are always centered on the tables, the FANUC CRX 10iA is the ideal choice for its balance of reach, payload, ease of use, and cost-effectiveness. However, if the workpieces are occasionally off-center, the Doosan H2515 would be preferable due to its extended reach, despite the higher cost. This approach allows the client flexibility in selecting the best option based on their budget and exact setup needs.


---

## Question 2: What gripper or grippers do you think would work for this solution?

### Answer:
For this solution, the OnRobot VG10 Vacuum Gripper would be a suitable choice for handling both workpieces—a 7 kg cardboard box and a 0.5 kg wooden cube.

### Reasoning:
High Payload Capacity: The VG10 gripper can handle payloads up to 15 kg, which exceeds the 7 kg requirement for the cardboard box. This capability ensures that it can securely lift the larger, heavier box without strain, maintaining stability during transport.

Adaptability for Different Shapes and Sizes: The VG10’s vacuum system allows for flexible suction cup arrangements, which makes it versatile for handling workpieces with varying dimensions. For the large cardboard box, the suction cups can be configured to distribute the load across the box’s surface, ensuring a secure grip. For smaller objects like the wooden cube, fewer suction cups can be activated to create a focused suction area, providing the precision needed for lighter items.

Tool-Less Changeover: Since the VG10 operates using vacuum suction, there’s no need to switch tools between the two workpieces, satisfying the client's requirement for an easy and toolless process. The operator can easily switch between picking up the larger box and the smaller cube without manual adjustments or tool swaps, making it a streamlined option for daily operations.

Easy Integration with Collaborative Robots: The VG10 is designed for compatibility with popular collaborative robots, including models like the Doosan and UR series. This integration is typically plug-and-play, allowing for straightforward setup and programming, which aligns with the client's preference for a user-friendly, programmable interface.

In summary, the OnRobot VG10 Vacuum Gripper is ideal for this application due to its high payload capacity, flexible suction configuration, ease of use, and compatibility with collaborative robots. These features make it a versatile and efficient choice for handling both the large cardboard box and the small wooden cube without requiring frequent adjustments.

---

## Question 3: Describe the calibration procedure that an operator can go through on a daily basis after moving the tables in the application footprint.


## Calibration Procedure Using Markers or Jigs (Corners and Middle of the Tables)

### 1. Set the Robot to Home Position:
Start by moving the robot to a known "home" position within its workspace. This position serves as a consistent baseline reference for the calibration.

### 2. Place Markers or Jigs on Calibration Points:
- **If using markers:** Place visual markers at the **corners** (one at a corner of each table) and at the **middle** of each table. These markers should be easily distinguishable, such as colored tape or dots.
- **If using positioning jigs:** Place custom-designed jigs at the **corner** and **middle** points of each table. The jigs should fit the robot’s end effector for precise alignment.

### 3. Manually Guide the Robot to Calibration Points:
- **With markers:** Use the robot’s teach pendant to move the end effector over each marker on the tables. Carefully align the end effector above the marker at the corner, verify the position, and record the coordinates. Repeat the process for the middle of each table.
- **With jigs:** Use the teach pendant to move the robot to the **corner jig** on Table A, aligning the end effector precisely. Once in place, record the coordinates. Repeat the same for the **middle jig** on Table A. Then move to Table B and repeat the same process for the corner and middle jigs.

### 4. Save the Calibration Points:
Record the coordinates for each table’s calibration points in the robot’s control software. These saved coordinates are now set as the robot’s reference for pick-up and placement tasks. Ensure you save the corner and middle points for both tables.

### 5. Verify Calibration Accuracy:
Run a quick pick-and-place test to ensure alignment accuracy. The robot should reach the target positions (corner and middle) correctly on each table.

---

## Optional question: What are the restrictions and internal safeguards of the cobot that allows it to be used without any other external safeguard?


### Answer:
#TODO

### Reasoning:
#TODO

---

## Challenges

List any challenges or obstacles you encountered while completing the tasks, and how you overcame them. 

---

## Conclusion

Summarize the approach taken to solve the tasks, the key takeaways, and any suggestions for future improvements or extensions.

---

## Additional Notes

If you have any additional information, such as further clarifications or improvements you would suggest, include them here.

