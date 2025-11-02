# Artificial-Intelligence-experiments-codes

《人工智能方法》课程的两个实验代码，八数码和决策树。Two experiment codes from the Artificial Intelligence Methods course: the Eight Puzzle and Decision Tree.

**文件说明与使用示例**

- `8_puzzle_Astar.cpp`：
	- 说明：使用 C++ 实现的 A* 算法求解 8-puzzle（八数码）问题，启发函数为曼哈顿距离。程序从标准输入读取初始状态与目标状态（各 3 行，每行 3 个以空格分隔的整数，0 表示空格），输出解的步数与每一步的状态序列。
	- 注意：此 C++ 实现**不检查可解性**（即不会判断输入是否有解）。在输入不可解的情况下程序行为可能不符合预期或无解时未给出提示，使用时请先确认输入可解或自行添加可解性检查。
	- 输入示例（stdin）：
		```
		1 2 3
		4 0 5
		6 7 8
		1 2 3
		4 5 6
		7 8 0
		```
	- 输出示例（stdout，格式示例）：
		```
		4
		1 2 3
		4 0 5
		6 7 8

		1 2 3
		4 5 0
		6 7 8

		1 2 3
		4 5 6
		0 7 8

		1 2 3
		4 5 6
		7 0 8

		1 2 3
		4 5 6
		7 8 0
		```

- `8_puzzle_Astar.py`：
	- 说明：使用 Python 实现的 A* 求解器（面向教学、少量拓展），默认目标状态为 `[[1,2,3],[8,0,4],[7,6,5]]`（代码内固定）。运行时从标准输入读取初始 3×3 状态（3 行），会检查可解性并打印求解路径（每一步的棋盘、深度和启发值）。
	- 输入示例（stdin）：
		```
		1 2 3
		8 0 4
		7 6 5
		```
	- 输出示例（stdout，若初始即为目标）：
		```
		[1, 2, 3]
		[8, 0, 4]
		[7, 6, 5]
		deep: 0
		h: 0
		-------------------------------------------
		```

- `8_puzzle_bfs.cpp`：
	- 说明：使用 C++ 实现的广度优先搜索（BFS）求解 8-puzzle。输入格式与 `8_puzzle_Astar.cpp` 相同（先初始状态再目标状态，各 3 行）。适用于步数较小或用于比较算法表现。
	- 注意：此 C++ 实现**不检查可解性**。对于不可解输入，程序可能无法正常返回结果或不提示无解，请在使用前确认输入可解。
	- 输入/输出示例：与 `8_puzzle_Astar.cpp` 相同的输入格式，输出为步数与解序列板块（每个中间状态按 3 行显示）。

- `ID3_decision_tree.py`：
	- 说明：一个简单的 ID3 决策树实现。默认读取仓库根目录下的 `traindata.txt` 作为训练集和 `testdata.txt` 作为测试集（文件中每行以空格分隔，最后一项为类别标签）。程序训练决策树并在测试集上输出误分类样例与准确率，同时可以绘制并展示一棵决策树的可视化图（使用 matplotlib）。
	- 运行示例：
		```
		python ID3_decision_tree.py
		```
	- 输出示例（stdout）：
		```
		误分类：
		数据： [2.0, 1.0, 3.0, 2] 误分类为：1
		准确率：0.875
		```
	- 可视化：
       ![](example\ID3_Decision_Tree_Example.png)

**运行/编译提示**

- Python：
	- 依赖：`numpy`, `matplotlib`（若未安装，请使用 `pip install numpy matplotlib`）。
	- 运行：
		```powershell
		python ID3_decision_tree.py
		python 8_puzzle_Astar.py
		```

- C++：
	- 使用 MinGW/g++（仓库在 Windows 下示例）。在命令行编译并运行：
		```powershell
		g++ -std=c++17 -O2 8_puzzle_Astar.cpp -o 8_puzzle_Astar.exe
		.\8_puzzle_Astar.exe < input.txt

		g++ -std=c++17 -O2 8_puzzle_bfs.cpp -o 8_puzzle_bfs.exe
		.\8_puzzle_bfs.exe < input_with_goal.txt
		```

**许可证**

本项目采用 MIT 许可证（MIT）。

版权所有 (c) 保留

简短声明：本仓库代码以教学与学习为目的，任何人均可在遵循 MIT 许可证条款下使用、复制、修改、合并、发布、分发、再许可及/或出售本软件的副本。

----

English version

# Artificial-Intelligence-experiments-codes

Two experiment codes from the Artificial Intelligence Methods course: the Eight Puzzle and Decision Tree.

**Files and Usage Examples**

- `8_puzzle_Astar.cpp`:
	- Description: A C++ implementation of A* for the 8-puzzle using Manhattan distance as the heuristic. The program reads the initial state and the goal state from stdin (each state is 3 lines, each line contains 3 space-separated integers; 0 denotes the blank). It outputs the solution length and the sequence of states along the path.
	- Note: This C++ implementation does NOT check solvability. For unsolvable inputs the program may not behave as expected or may not report 'no solution'. Please ensure inputs are solvable or add a solvability check before use.
	- Input example (stdin):
		```
		1 2 3
		4 0 5
		6 7 8
		1 2 3
		4 5 6
		7 8 0
		```
	- Output example (stdout):
		```
		4
		1 2 3
		4 0 5
		6 7 8

		1 2 3
		4 5 0
		6 7 8

		1 2 3
		4 5 6
		0 7 8

		1 2 3
		4 5 6
		7 0 8

		1 2 3
		4 5 6
		7 8 0
		```

- `8_puzzle_Astar.py`:
	- Description: A Python A* solver intended for teaching and light modification. The goal state is fixed in the code as `[[1,2,3],[8,0,4],[7,6,5]]`. The program reads an initial 3×3 state from stdin (3 lines) and checks solvability; it prints the solution path (each state's board, depth and heuristic value).
	- Input example (stdin):
		```
		1 2 3
		8 0 4
		7 6 5
		```
	- Output example (stdout, when the initial state is the goal):
		```
		[1, 2, 3]
		[8, 0, 4]
		[7, 6, 5]
		deep: 0
		h: 0
		-------------------------------------------
		```

- `8_puzzle_bfs.cpp`:
	- Description: A C++ breadth-first search (BFS) solver for the 8-puzzle. Input format is the same as `8_puzzle_Astar.cpp` (initial state, then goal state; each is 3 lines). Suitable for small solution depths or for comparing algorithm behavior.
	- Note: This C++ implementation does NOT check solvability. For unsolvable inputs the program may not behave as expected or may not report 'no solution'. Please ensure inputs are solvable or add a solvability check before use.
	- Input/output examples: same input format as `8_puzzle_Astar.cpp`. Output includes the number of steps and the sequence of intermediate states (each state printed as 3 lines).

- `ID3_decision_tree.py`:
	- Description: A simple ID3 decision tree implementation. By default it reads `traindata.txt` (training data) and `testdata.txt` (test data) from the repository root. Each line should contain features separated by spaces, with the last entry being the class label. The program trains a decision tree, prints misclassified examples and accuracy on the test set, and can display a visualization of the learned tree using matplotlib.
	- Run example:
		```
		python ID3_decision_tree.py
		```
	- Output example (stdout):
		```
		Misclassified:
		Data: [2.0, 1.0, 3.0, 2] misclassified as: 1
		Accuracy: 0.875
		```
	- Visualization: 
        ![](example\ID3_Decision_Tree_Example.png)
**Build / Run Notes**

- Python:
	- Dependencies: `numpy`, `matplotlib` (install with `pip install numpy matplotlib` if needed).
	- Run:
		```powershell
		python ID3_decision_tree.py
		python 8_puzzle_Astar.py
		```

- C++:
	- Use MinGW/g++ on Windows (example). To compile and run:
		```powershell
		g++ -std=c++17 -O2 8_puzzle_Astar.cpp -o 8_puzzle_Astar.exe
		.\8_puzzle_Astar.exe < input.txt

		g++ -std=c++17 -O2 8_puzzle_bfs.cpp -o 8_puzzle_bfs.exe
		.\8_puzzle_bfs.exe < input_with_goal.txt
		```

**License**

This project is released under the MIT License.

Copyright (c)

Short statement: This repository's code is intended for teaching and learning. Anyone may use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software under the terms of the MIT License.