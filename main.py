'''def select_activities(start_times, finish_times):
  n = len(start_times)

  # Create a list of (start, finish, activity_index) tuples
  activities = [(start_times[i], finish_times[i], i) for i in range(n)]

  # Sort activities by their finish times
  activities.sort(key=lambda x: x[1])

  selected_activities = []
  last_activity = activities[0]

  # Select the first activity
  selected_activities.append(last_activity[2])
  total_finish_time = last_activity[1]

  for i in range(1, n):
      current_activity = activities[i]

      if current_activity[0] >= last_activity[1]:
          selected_activities.append(current_activity[2])
          total_finish_time += current_activity[1]
          last_activity = current_activity

  return selected_activities, total_finish_time

# Function to print selected activities and total finish time
def print_selected_activities(start_times, finish_times):
  selected_activity_indices, total_finish_time = select_activities(start_times, finish_times)

  print("Selected Activities:")
  for index in selected_activity_indices:
      print(f"Activity from {start_times[index]} to {finish_times[index]}")
  print("Total finish time for optimal activities:", total_finish_time)
  print()

# Test the function with multiple input sets
start_times_sets = [[10, 12, 20], [1,3,0,5,8,5], [9,4,1,2,5,8,10,2,2,3], [10,12,20]]
finish_times_sets = [[20,25,30], [2,4,6,7,9,9], [12,14,13,20,12,18,19,18,12,15],[20,25,30]]

for i in range(len(start_times_sets)):
  print(f"Set {i + 1}:")
  print_selected_activities(start_times_sets[i], finish_times_sets[i])

'''

def optimal_selection(activities):
  n = len(activities)
  selected = [False] * n

  # Sort activities by their finish times
  activities.sort(key=lambda x: x[2])

  last_finish_time = activities[0][2]
  count = 1

  # Greedily select non-overlapping activities
  for i in range(1, n):
      if activities[i][0] >= last_finish_time:
          selected[i] = True
          last_finish_time = activities[i][2]
          count += 1

  return selected, count

def calculate_ratio(activities):
  # Run the optimal selection algorithm
  selected_optimal, optimal_count = optimal_selection(activities)

  # Run the greedy algorithm (same as optimal_selection function)
  selected_greedy, greedy_count = optimal_selection(activities)

  # Calculate the ratio
  ratio = optimal_count / greedy_count

  return ratio

# Example activities for n = 3
activities = [
  (0, 2, 3, 3, 6),
  (6, 8, 9, 12, 15),
  (12, 14, 15, 15, 18)
]

ratio = calculate_ratio(activities)
print("Ratio of activities chosen by optimal solution to greedy algorithm:", ratio)
