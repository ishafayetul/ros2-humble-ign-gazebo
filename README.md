
# 🚀 Gazebo Ignition (Fortress+) Beginner Cheat Sheet

## 📦 Installing Ignition
```bash
sudo apt update
sudo apt install gazebo -y            # Or specific version: ignition-fortress
```

---

## 🧠 Key Concepts
- **World**: Simulation environment
- **Model**: Robots or objects in the world
- **Topic**: Communication channel (Pub/Sub)
- **Service**: Request/Response actions
- **Component**: Runtime properties of entities
- **Entity**: Model, light, or sensor with a unique ID

---

## 🏁 Launching Gazebo
```bash
ign gazebo <your_world>.sdf           # Launch world
ign gazebo -r <your_world>.sdf        # Run headless
ign gazebo -g <plugin>.so <world>     # With plugin
```

---

## 🔧 Ignition Topic Commands
### 📋 List Topics
```bash
ign topic -l
```

### ℹ️ Get Info About a Topic
```bash
ign topic -i -t /topic_name
```

### 📺 Echo Topic Messages
```bash
ign topic -e -t /topic_name
# Optional:
ign topic -e -t /topic_name -n 5      # Show 5 messages
ign topic -e -t /topic_name -d 10     # Show messages for 10 seconds
```

### 📤 Publish to a Topic
```bash
ign topic -t /topic_name -m <msg_type> -p '<message>'
# Example:
ign topic -t /cmd_vel -m ignition.msgs.Twist -p 'linear: {x: 1.0}'
```

---

## 🔍 Entity Introspection
### List All Entities
```bash
ign model -l
```

### Get Model Info
```bash
ign model -m <model_name> -i
```

---

## 🛠 Useful Ignition Tools
| Command         | Description                    |
|----------------|--------------------------------|
| `ign gazebo`   | Launch simulation              |
| `ign topic`    | Topic interaction (pub/sub)    |
| `ign model`    | Model info & spawning          |
| `ign service`  | Interact with services         |
| `ign fuel`     | Download models from Fuel      |
| `ign physics`  | Control physics engines        |

---

## 🔁 Example Workflow
1. Launch Gazebo:
   ```bash
   ign gazebo my_world.sdf
   ```
2. List topics:
   ```bash
   ign topic -l
   ```
3. Echo a topic:
   ```bash
   ign topic -e -t /clock
   ```
4. Publish a command:
   ```bash
   ign topic -t /model/robot1/cmd_vel -m ignition.msgs.Twist -p 'linear: {x: 0.5}'
   ```

---

## 📚 Learn More
- [Ignition Robotics Docs](https://gazebosim.org/docs)
- [Ignition Fuel Models](https://app.gazebosim.org/)
