<table>
  <tr>
    <th>Name</th><th>TC-1: E2E: Event CRUD operations</th>
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
    <th>Autor</th>
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
          <td>Press + button.</td>
          <td>User can see blank screen with next buttons: Task, Event.</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Press event button.</td>
          <td>
            <ul>
              <li>Event creation screen is opened.</li>
              <li>"All day" toggle option is deselected.</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>3</td>
          <td>
            <ol>
              <li>Fill name field with "TestEvent" string.</li>
              <li>Switch "All day" toggle on.</li>
              <li>Select current date.</li>
              <li>Press Save button.</li>
            </ol>
          </td>
          <td>
            <ul>
              <li>Event creation screen is closed.</li>
              <li>User can see calendar grid with event icon in current date cell.</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <th>Postconditions</th>
    <td>...</td>
  </tr>
  <tr>
    <th>Environment</th>
    <td>...</td>
  </tr>
</table>
