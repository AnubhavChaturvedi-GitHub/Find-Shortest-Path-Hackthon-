# Shortest Path Finder in Random Graphs

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Instagram][instagram-shield]][instagram-url]
[![Twitter][twitter-shield]][twitter-url]
[![YouTube][youtube-shield]][youtube-url]
[![Telegram][telegram-shield]][telegram-url]

![Shortest Path Finder](https://github.com/user-attachments/assets/3ddbaca8-1a50-4c0f-bb23-f7cafaf17d8b)

## 🚀 Project Overview

This project demonstrates an algorithm that finds the shortest path between two nodes in a randomly generated graph. It was developed as part of a hackathon, and it earned a spot in the top 10 projects, proudly powered by the Honeybell team.

## 📝 Problem Statement

Given a randomly generated graph, the goal is to find the shortest path between two specified nodes. The algorithm explores all possible paths between the nodes, measures their lengths, and identifies the shortest path.

## ⚙️ How It Works

1. **Graph Generation:** A random graph is generated with nodes and edges. The graph can represent various networks, such as city maps, network topologies, or any other connectable data points.

2. **Input Nodes:** The user inputs the start and end nodes between which the shortest path needs to be determined.

3. **Path Exploration:** The algorithm explores all possible paths between the start and end nodes using traversal techniques. It checks every path to ensure no possible route is missed.

4. **Path Length Calculation:** For each path found, the algorithm calculates its total length.

5. **Shortest Path Identification:** Among all the explored paths, the algorithm selects and displays the path with the minimum length.

## 🧑‍💻 Algorithm Description

The algorithm is designed as follows:

1. **Graph Representation:** The graph is represented using an adjacency list or matrix, capturing all nodes and their connections.
   
2. **Traversal Method:** It employs a traversal method like Depth-First Search (DFS) or Breadth-First Search (BFS) to explore all paths between the two input nodes.

3. **Path Validation:** Each path is validated to ensure it connects the two nodes without revisiting any node unnecessarily.

4. **Path Length Calculation:** The algorithm sums the weights or counts the edges of each path to determine its length.

5. **Comparison:** All path lengths are compared, and the shortest one is displayed as the output.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Libraries:** NetworkX (for graph generation and manipulation), Matplotlib (for visualization), and other standard libraries.

## 🚩 Features

- Generates a random graph with dynamic nodes and edges.
- Finds and displays the shortest path between two user-defined nodes.
- Visually represents the graph and paths for better understanding.
- Efficiently calculates all paths and compares their lengths.
  
## 🥇 Achievements

This project was selected in the top 10 at the Hackathon event and was powered by the Honeybell team, showcasing the innovative approach to solving shortest path problems using graph theory.

## 📊 Use Cases

- **Navigation Systems:** Finding the shortest route between locations.
- **Network Optimization:** Optimizing data paths in networks.
- **Game Development:** Determining paths in game maps.
- **Logistics:** Route optimization for delivery services.

## 🔥 Getting Started

To run this project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AnubhavChaturvedi-GitHub/Find-Shortest-Path.git
   cd Find-Shortest-Path
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Algorithm:**
   ```bash
   python shortest_path_finder.py
   ```

4. **Input Nodes:** Enter the start and end nodes when prompted.

5. **View Results:** The shortest path will be displayed along with the graph visualization.

## 🤝 Collaboration and Future Work

Contributions, issues, and feature requests are welcome! Future improvements may include:
- Enhancing the efficiency of pathfinding with advanced algorithms like Dijkstra or A*.
- Adding a user-friendly graphical interface for better interaction.

## 📢 Acknowledgments

This project would not have been possible without the support of the Honeybell team and the amazing opportunities provided during the Hackathon.


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0B5FBB
[linkedin-url]: https://www.linkedin.com/in/anubhav-chaturvedi-/

<!-- Instagram -->

[instagram-shield]: https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white
[instagram-url]: https://www.instagram.com/_anubhav__chaturvedi_/

<!-- Twitter -->

[twitter-shield]: https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white
[twitter-url]: https://x.com/AnubhavChatu


<!-- YouTube -->
[youtube-shield]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[youtube-url]: https://www.youtube.com/@NetHyTech

<!-- Telegram -->
[telegram-shield]: https://img.shields.io/badge/Telegram-%231DA1F2.svg?style=for-the-badge&logo=Telegram&logoColor=white
[telegram-url]: https://t.me/YourTelegramUsername

