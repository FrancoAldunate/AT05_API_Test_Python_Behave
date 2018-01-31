Feature: Search music
  Search songs by artist in Spotify

  Scenario: Search songs by artist
    Given I select these artists
      | name            | birth   |
      | Michael Jackson | August 29, 1958 |
      | Elvis           | January 8, 1935 |
      | John Lennon     | October 9, 1940 |
    When I choose option search
    Then A list of songs of each artist should be shown
