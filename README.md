# Crab Bot: Optimizing Vertical Motion for Existing Warehouse Shelving

Demo Video: https://youtu.be/4HDuLfcB2LA

<img width="382" alt="image" src="https://github.com/user-attachments/assets/19ec1b20-e35c-4be8-b279-49ab009df2d3" />


## Inspiration
The inspiration for CrabBot came from a clear gap we identified in the existing landscape of robotic solutions for distribution centers. Despite major advancements in automation, the vast, towering shelves within these warehouses remain inaccessible to ground-based robots. Existing solutions like Exotec Solutions’ SkyPod and BionicHive’s Squid made vertical mobility possible, but they came with significant limitations: high costs, infrastructure complexity, and a lack of adaptability to diverse warehouse setups. We wanted to design a solution that could overcome these barriers, offering both vertical mobility and a low-cost, easy-to-integrate design. CrabBot was born from this desire to innovate and bridge the gap between technology and practical implementation in real-world environments.

## How we built it

### Initial Conceptualization:
We started by researching existing robotic systems in warehouse environments and identified the key pain points related to vertical motion. We knew that for our solution to succeed, it needed to be both cost-effective and easy to integrate into current warehouse setups. Taking into account the experience of the team members, we approached our solution with an intent to submit to the beginner and amazon tracks.

### Designing the Mechanism:
We designed a modular robot with a unique vertical movement system using gears that mesh with a rail attached to shelves. The system would allow CrabBot to climb vertically, with stability ensured through strategically placed bearings. The floating design offered reduced friction and minimized wear, making the system more reliable and less maintenance-intensive.

### Prototyping:
We built a working prototype that demonstrated the robot’s ability to move vertically on existing shelving. The modular design allowed for easy adjustments and experimentation with different rail and gear configurations, helping refine the robot’s performance.

### Testing:
After building the prototype, we conducted several rounds of testing in various simulated warehouse environments. The robot’s ability to move vertically without significant infrastructure changes was a success. However, we faced challenges with fine-tuning the stability during vertical motion, which required modifying the bearing system to better support the weight distribution.

### Refining the Design:
The final design incorporated feedback from testing, with improvements in the gear mechanism for smoother movement and a more durable rail system. The final product was able to climb efficiently, securely attach to rails, and operate with minimal maintenance.

## Challenges we ran into

### Stability and Movement Precision:
The initial design faced issues with stability when moving vertically. Ensuring that the robot could navigate taller shelves without wobbling or losing stability required extensive trial and error in selecting the right bearings and materials.

### Integration with Existing Infrastructure:
A significant challenge was ensuring that the robot could integrate smoothly into existing warehouse setups. It was critical that the rail system could be easily installed without requiring extensive modifications to the shelves. The modular nature of the system was key in overcoming this challenge, but there were still concerns about the ease of installation, which required careful consideration during the design phase.

### Cost-Effectiveness:
Maintaining a low-cost approach while ensuring reliability was a constant balancing act. We had to carefully select components that provided the best performance at a reasonable price, keeping in mind that high upfront costs could limit the adoption of the solution.

### Prototyping Materials:
A large reason for the robot's final form, with both motion on the ground and on the rail controlled by explicit instruction, was due to core difficulties we experienced with the available hardware materials. Firstly, without the proper motor controllers, our omni-directional wheels were unable to be fully used. We were able to learn more about different alternatives to driving these motors from constructing custom H-bridges to using Relays to change the motor's direction. We adapted to this by only driving the robot side to side for  locking into the rail system. Secondly, the Raspberry Pi Model 2B we used had trouble downloading the full capabilities of the visual detection tools we desired, hindering our ability to utilize barcode and ArUco tags for shelf and bin alignment. Finally, the geared DC motor given to us for our climbing mechanism was not a high enough gear ratio to provide enough torque to go up the shelf. 

Despite these challenges, which hindered our ability to implement a fully autonomous driving and climbing system, we were able to design and build a robust, cheap, and scalable solution for large shelf autonomous navigation.

## What we learned
Building CrabBot taught us several crucial lessons about design, innovation, and problem-solving in robotics. We learned the importance of modularity and simplicity in engineering solutions, especially when aiming for scalability and ease of implementation in existing infrastructure. We also gained a deeper understanding of how even small design choices—like the integration of a gear-rail system for vertical movement—can lead to more robust, cost-effective solutions. Additionally, we realized the power of creating a solution that is adaptable and can easily integrate into existing systems, reducing the need for major overhauls in a warehouse setting.
