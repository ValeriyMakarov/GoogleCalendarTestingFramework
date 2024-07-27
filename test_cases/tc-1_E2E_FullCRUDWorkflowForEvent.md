<table>
  <tr>
    <th>Name</th><th>TC-1: E2E: Full CRUD Workflow for events</th>
  </tr>
  <tr>
    <th>Description</th>
    <td>The aim of the test is to check functionality of all main operations (Create, Read, Update, Delete) of event feature.</td>
  </tr>
  <tr>
    <th>References</th>
    <td></td>
  </tr>
  <tr>
    <th>Author</th>
    <td>Me</td>
  </tr>
  <tr>
    <th>Priority</th>
    <td>P0</td>
  </tr>
  <tr>
    <th>Severity</th>
    <td>S0</td>
  </tr>
  <tr>
    <th>Preconditions</th>
    <td>
      <ol>
        <li>Open Google Calendar.</li>
        <li>Select month enents show type.</li>
        <li>User can see calendar grid.</li>
        <li>There are no events in the grid.</li>
      </ol>
    </td>
  </tr>
  <tr>
    <th>Steps</th>
    <td>
      <table>
        <tr>
          <th>№</th>
          <th>Step</th>
          <th>Expected result</th>
        </tr>
        <tr>
          <td>1</td>
          <td>Press "+" button.</td>
          <td>User can see screen with next buttons: Task, Event.</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Press event button.</td>
          <td>Event creation screen is opened.</td>
        </tr>
        <tr>
          <td>3</td>
          <td>Fill name field with "TestEvent" string.</td>
          <td>Done.</td>
        </tr>
        <tr>
          <td>4</td>
          <td>Select current date and time.</td>
          <td>Done.</td>
        </tr>
        <tr>
          <td>5</td>
          <td>Press Save button.</td>
          <td>
            <ul>
              <li>Event creation screen is closed.</li>
              <li>User can see calendar grid with event icon in current date cell.</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>6</td>
          <td>Press on current day cell.</td>
          <td>
            <ul>
              <li>Screen with day schedule view is opened.</li>
              <li>User can see event with "TestEvent" name.</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>7</td>
          <td>Press on event.</td>
          <td>User can see event info screen.</td>
        </tr>
        <tr>
          <td>8</td>
          <td>Press edit button.</td>
          <td>Event creation screen is opened.</td>
        </tr>
        <tr>
          <td>9</td>
          <td>Change name to "New TestEvent".</td>
          <td>Done.</td>
        </tr>
        <tr>
          <td>10</td>
          <td>Press Save button.</td>
          <td>
            <ul>
              <li>Event creation screen is closed.</li>
              <li>User can see calendar day schedule view with event with "New TestEvent" name.</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>11</td>
          <td>Press on event.</td>
          <td>User can see event info screen.</td>
        </tr>
        <tr>
          <td>12</td>
          <td>Press Kebab menu button.</td>
          <td>User can see kebab menu.</td>
        </tr>
        <tr>
          <td>13</td>
          <td>Press Delete button.</td>
          <td>User can see deletion alert with Cancel, Delete options.</td>
        </tr>
        <tr>
          <td>14</td>
          <td>Press Delete button.</td>
          <td>
            <ul>
              <li>Event creation screen is closed.</li>
              <li>User can see calendar day schedule view without event with "New TestEvent" name.</li>
            </ul>  
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <th>Postconditions</th>
    <td>
      <ul>
        <li>There are no events left in the calendar.</li>
        <li>Close Google Calendar.</li>
        <li>User should be redirected to the Home page.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Environment</th>
    <td>Android 11.0</td>
  </tr>
</table>
