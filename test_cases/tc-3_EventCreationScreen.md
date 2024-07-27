<table>
  <tr>
    <th>Name</th><th>TC-2: Event creation screen.</th>
  </tr>
  <tr>
    <th>Description</th>
    <td>The aim of the test is to check localization of event creation screen.</td>
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
    <td>P1</td>
  </tr>
  <tr>
    <th>Severity</th>
    <td>S3</td>
  </tr>
  <tr>
    <th>Preconditions</th>
    <td>
      <ol>
        <li>Open Google Calendar.</li>
        <li>Select month enents show type.</li>
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
          <td>Open event creation screen.</td>
          <td>
            User can see screen with next fields:
            <ol>
              <li>Field name: "Title", Field text: "Add title".</li>
              <li>Field name: "Event button", Field text: "Event".</li>
              <li>Field name: "Task button", Field text: "Task".</li>
              <li>Field name: "All day switch", Field text: "All day".</li>
              <li>Field name: "Start time", Field text: {day and time in selected format}.</li>
              <li>Field name: "End time", Field text: {day and time in selected format}.</li>
              <li>Field name: "Timezone", Field text: {timezone}.</li>
              <li>Field name: "Does not repeat button", Field text: "Does not repeat".</li>
              <li>Field name: "Add guests button", Field text: "Add guests".</li>
              ...
            </ol>
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
