import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def judges_age():
  # Load the CSV file into a pandas DataFrame
  judges_df = pd.read_csv('judges.csv')

  # Convert 'Birth Year' to numeric and 'Commission Date (1)' to datetime
  judges_df['Birth Year'] = pd.to_numeric(judges_df['Birth Year'],
                                          errors='coerce')
  judges_df['Commission Date (1)'] = pd.to_datetime(
      judges_df['Commission Date (1)'], errors='coerce')

  # Calculate age at commission
  judges_df['Age at Commission'] = judges_df[
      'Commission Date (1)'].dt.year - judges_df['Birth Year']

  # Group by the year of commission and calculate the average age at commission
  average_age_by_commission_year = judges_df.groupby(
      judges_df['Commission Date (1)'].dt.year)['Age at Commission'].mean(
      ).reset_index()

  # Set the current date for the analysis
  current_date = datetime.now()

  # Convert 'Senior Status Date (1)' and 'Termination Date (1)' to datetime, if they exist
  judges_df['Senior Status Date (1)'] = pd.to_datetime(
      judges_df['Senior Status Date (1)'], errors='coerce')
  judges_df['Termination Date (1)'] = pd.to_datetime(
      judges_df['Termination Date (1)'], errors='coerce')

  # Calculate the 'end of service' date as the earliest of the senior status date, termination date, or current date
  judges_df['End of Service Date'] = judges_df[[
      'Senior Status Date (1)', 'Termination Date (1)'
  ]].min(axis=1)
  judges_df['End of Service Date'] = judges_df['End of Service Date'].fillna(
      current_date)

  # Create a range of years from the earliest commission date to the current year
  years = range(judges_df['Commission Date (1)'].min().year,
                current_date.year + 1)

  # Initialize a list to hold the average age data for each year
  average_age_each_year_list = []

  # Calculate the average age for each year
  for year in years:
    # Find judges who were active at any point during the year
    active_judges = judges_df[
        (judges_df['Commission Date (1)'].dt.year <= year)
        & (judges_df['End of Service Date'].dt.year >= year)].copy()

    # Calculate their age at the end of that year
    active_judges.loc[:,
                      'Age at End of Year'] = year - active_judges['Birth Year']

    # Calculate the average age
    average_age = active_judges['Age at End of Year'].mean()

    # Append to the list
    average_age_each_year_list.append({
        'Year': year,
        'Average Age': average_age
    })

  # Convert list of dicts to DataFrame
  average_age_each_year = pd.DataFrame(average_age_each_year_list)

  # Plotting the average age of judges at the time of their commission over time
  plt.figure(figsize=(14, 7))
  plt.subplot(1, 2, 1)
  plt.plot(average_age_by_commission_year['Commission Date (1)'],
           average_age_by_commission_year['Age at Commission'],
           marker='o',
           linestyle='-',
           color='green')
  plt.title('Average Age at Time of Commission Over Time')
  plt.xlabel('Year of Commission')
  plt.ylabel('Average Age')
  plt.grid(True)

  # Plotting the average age of currently active judges each year
  plt.subplot(1, 2, 2)
  plt.plot(average_age_each_year['Year'],
           average_age_each_year['Average Age'],
           marker='o',
           linestyle='-',
           color='purple')
  plt.title('Average Age of Currently Active Judges Each Year')
  plt.xlabel('Year')
  plt.ylabel('Average Age')
  plt.grid(True)

  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
  judges_age()
