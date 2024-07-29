<table>
  <tr>
    <th>Name</th><th>TC-2: Event creation via plus button.</th>
  </tr>
  <tr>
    <th>Description</th>
    <td>The aim of the test is to check functionality of event creation via plus button.</td>
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
    <td>S1</td>
  </tr>
  <tr>
    <th>Preconditions</th>
    <td>
      <ol>
        <li>Open Google Calendar.</li>
        <li>Select month events show type.</li>
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
          <td>User can see screen with next buttons: Reminder, Event, Goal.</td>
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
          <td>Press "Does not repeat" button and select "Every day" option in dialog.</td>
          <td>
            <ul>
              <li>Dialog is closed.</li>
              <li>"Does not repeat" button changed text to "Every day".</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>6</td>
          <td>Add a guest using "test_guest@gmail.com" email.</td>
          <td>
            <ul>
              <li>User can see the list of guests.</li>
              <li>User can see that video google conference info is added.</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td>7</td>
          <td>Press "Add rooms or location" button and select Odessa, Ukraine.</td>
          <td>User can see location info.</td>
        </tr>
        <tr>
          <td>8</td>
          <td>Add new notification "in 20 minutes".</td>
          <td>User can see notification "in 20 minutes" in the notifications list.</td>
        </tr>
        <tr>
          <td>9</td>
          <td>Select Banana color of event.</td>
          <td>User can see that event color text is "Banana".</td>
        </tr>
        <tr>
          <td>10</td>
          <td>Add description text "Text123".</td>
          <td>User can see "Text123" in the field.</td>
        </tr>
        <tr>
          <td>11</td>
          <td>Attach a file.</td>
          <td>User can see attached file in the attachments list.</td>
        </tr>
        <tr>
          <td>12</td>
          <td>Press Save button.</td>
          <td>Allert with text "Send to guests..." and "Send", "Don't send" and "Cancel" options is appeared.</td>
        </tr>
        <tr>
          <td>12</td>
          <td>Press "Don't send" button.</td>
          <td>
            <ul>
              <li>Event creation screen is closed.</li>
              <li>User can see calendar grid with event icon in current date cell.</li>
              <li>Toast with text "Saved..." is appeared.</li>
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
