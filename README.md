# Purpose
This repository is a POC for establishing the feasability of a communication between ROS 2 (with eProsima FastDDS DDS implementation) and RustDDS.

# Installation
I assume that you already installed ROS 2 Foxy, colcon and you have sourced the correct script (often /opt/ros2/foxy/setup.bash).
I'm using Visual Studio Code and Python 3.x.x, the .vscode will help you having correct path to the needed python ressources, essentially for vscode intellisense.

For the steps below, i assule you are in the root directory.

## Compile
```
colcon build --packages-select ros2_dummy_pkg --symlink-install
```

This will compile only the ros2_dummy_pkg (ros2 package).

## Source the local script
```
source install/local_setup.bash
```

This will source a script, allowing you to use ros2 commands with your package/node (in this case, ros2_dummy_pkg).

## Launch the node
```
ros2 run ros2_dummy_pkg node
```

## Helper script
Because it's so boring to do always the same several manipulations, i provide a script doing all the previous steps.

```
./build.sh
```

Also, if you are using visual studio code, you can execute a task i provided.
For that: Ctrl + B and select the "build ros2_dummy_pkg" task.


# Usage
I assume now that you have launched the ros2_dummy_pkg's node: node (didn't see that comming don't you ! :p)

## Topics
/dummy_node__pub : the topic the node will print to each second. The published message is "dummy node is publishing !"
/dummy_node__sub : the topic the node is listening

## The logs
The node automatically prints logs when receiving a message on the topic he's listening.

## CLI commands
### Listening /dummy_node__pub topic
```
ros2 topic echo /dummy_node__pub
```

### Sending to /dummy_node__sub topic
```
ros2 topic pub /dummy_node__sub example_interfaces/String "data: hi!"
```

# Deployment
This project is a POC, then no efforts has been made to make a production ready binary.
You can nevertheless pick the result of the colcon building here:
install/ros2_dummy_pkg/lib/ros2_dummy_pkg/
There will be a binary named "node"

You can execute it directly:
```
./install/ros2_dummy_pkg/lib/ros2_dummy_pkg/node
```
