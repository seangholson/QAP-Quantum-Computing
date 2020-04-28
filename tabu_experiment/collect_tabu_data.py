from tabu_experiment.rnp_qap import RunExperimentsAndPlotStatsQAP
from experiment_code.run_and_plot_TSP import RunExperimentsAndPlotStatsTSP

# Run this file from QAP-Quantum-Computing directory

# number of trials of experiment
num_trials = 2
# type of sampler, choose between 'QPU', 'SA', or 'Tabu'
sampler = 'Tabu'
# toggle the ability to save the csv that comes out of a set of experiments
save_csv = False

run_qap = RunExperimentsAndPlotStatsQAP(num_trials=num_trials, sampler=sampler, save_csv=save_csv)
# run_tsp = RunExperimentsAndPlotStatsTSP(num_trials=num_trials, sampler=sampler, save_csv=save_csv)

run_qap.run_experiments()
# run_tsp.run_experiments()

# plots for Hadley - Rendl time limit problems
run_qap.plot_iter_lim_had()
# run_tsp.plot_time_lim_had()

# plots for Nugent - Ruml time limit problems
run_qap.plot_iter_lim_nug()
# run_tsp.plot_time_lim_nug()
