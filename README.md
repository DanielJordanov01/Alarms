# Alarms
Report
1. Process json file – I’ve created a python script that converts the timestamps from the
original json file to dates and turns it into a dictionary where the key is the date. This is done
because a hashmap will be used for the react state and all the adding, deleting, and
retrieving processes will be much more efficient than using an array.
2. I am using github pages to divide the project into tickets. It helps me stay organized and
focused on the particular task.
3. In react I render the alarms based on their dates. The user can select dates from a calendar,
If there are no alarms a message will show telling that no alarms were found on this date. If
there are alarms they will be displayed sorted by time. If a user clicks on the name of the
alarm a dialog would open showing all the details of the alarm. If the alarm is confirmed it
will become green and no later actions can be performed on the particular item, if a user
decides to skip the alarm it will become slightly grayed and no further actions will be allowed
on the selected alarm.
4. I’ve given myself the freedom to create a custom logo for the project. It’s not necessary but
it certainly makes the app look better and more professional.

Running the project
To start the project clone the repository navigate to /client then run “npm install” in the
projects directory. After the installation of the packages is complete run “npm start” in the /client
directory. The app will start shortly
