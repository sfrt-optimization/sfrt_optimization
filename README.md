# sfrt_optimization
an open source repository for spatially fractionated radiation therapy treatment planning decision making optimization and analysis

* Note: path variable in `ingest/dicom_reader` must be changed to the relevant CT\RS\ file
* Note: maintain repository structure on implementation as repository is highly interdependent

## Installation

To run, download poetry with `pip install poetry`.

Once poetry is downloaded, configure virtual environment with `poetry install`.

After virtual environment has been created, activate with `poetry shell`.

### Running Ingest

To run ingest, make sure you are in the root directory `Research/`, and then execute `python ingest.py`.

## Description

### Running Models (Start Here)

The simplest way to quickly run a robust and effective model is to download the entire `sfrt_optimal_placement/` folder, place the structural dicom file in the `dicom_file/` folder (and only the rstruct file, not the folder of all slices) and execute `run_model.py`. Optimal coordiantes of centers will be placed in `Optimal_Points.csv` inside `sfrt_optimal_placement/`.

### primary pipeline

dicom_reader.py - creates a list of all points within a given ROI, prints to json file - requires `*_grid_placement.py` - writes .pkl files to `/data`
* Note: `relative_grid_placement.py`, `triangle_grid_placement.py`, and `grid_placement.py` (independent descritization method) can be selected by changing the import statement in `dicom_reader.py` The files run the same way with methods of the same names, only the import statement needs to be changed. 

parameter_writer.py - reads candidate_points.json, calculates nodes and arcs, writes node_data.pkl, arc_data.pkl, arc_list.pkl, adjacency_matrix.pkl, neighborhood.pkl files

arc_optimization.py - a preliminary implementation of the Maximum Independent Set problem in Gurobi, reads node_data.json and arc_data.json

**All model files require `data/` files created and updated by dicom_reader.py and parameter_writer.py

## Secondary Models

#### Other Optimization Models:

* Clique_Optimization.py : solves MIS problem using all maximal cliques rather than edges. Needs cliques.json from Clique_Problem.py
    
* Node_Optimization.py : solves MIS problem using aggregated constraints, such that there is only one adjacency constraint per node. Needs arc_list.json and node_data.json
To initialize env, run `poetry install`

* continuous_adjacency_optimizaton.py: solves with a continuous optimization model based off an adjacency matrix

* warm_start_optimization.py: utilizes a warm start heuristic to initialize branch and bound model

#### Heuristics:

* cube_heuristic.py : finds a solution for the MIS problem by assuming that the spheres all sit on a uniform grid, which is optimal for a rectangular shape. Finds every possible grid solution and returns best solution.
    
* Greedy_Algorithm.py : Implementation of a Greedy algorithm that performs suspiciously poorly. Needs validation, potentially correction.

* spherical_heuristic.py : finds a quality solution by implementing a continuous optimization over a sphere to initialize the model
    

## Other Files

* Clique_Problem.py - uses networkX library to find all cliques and create cliques.json. Requires node_data.json and arc_data.json

* grid_placement.py - containes helper funcitons for dicom_reader.py

* Structure_Visualizer.py - can be used to visualize ROIs in 3D and 2D slices



## Miscellaneous files

* cube_optimization.py - another implementation of the MIS problem to test computation time, data storage
* dicom_tester.py - reads dicom files, don't use
