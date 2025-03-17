import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

# user story 1
""" som en användare vill jag kunna se hur en daily scrum går till så att jag kan förbereda mig inför en daily scrum """
# klicka på knapen somwhere in middle 
# klicka på knappen vars text innehåller "daily scrum"
# kontrollera att man ser en rubrik med texten "Daily standup"

def test_view_daily_scrum_timer(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Navigate to daily standup
    button_locator = page.get_by_role("button")
    middle_button = button_locator.get_by_text("Somewhere in the middle")
    middle_button.click()
    
    daily_button = page.get_by_role("button").get_by_text("Daily standup") 
    daily_button.click()

    # Start timer
    start_button = page.get_by_role("button").get_by_text(" Start the standup: 10 minutes ")
    start_button.click()

    # Check timer display
    timer_span = page.locator("span.framed")
    expect(timer_span).to_be_visible()
    expect(timer_span).to_have_text(re.compile(r"\d+:\d+"))



# this is just för test purposes
def test_view_daily_scrum_last(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    button_locator = page.get_by_role("button")
    somwhreinmiddle = button_locator.get_by_text("Last")
    somwhreinmiddle.click()



def test_sprint_review_presentation(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    
    # Click Last button to navigate to Sprint Review section
    button_locator = page.get_by_role("button")
    last_button = button_locator.get_by_text("Last")
    last_button.click()
    
    # Click Sprint Review button
    sprint_review_button = page.get_by_role("button").get_by_text("Sprint review")
    sprint_review_button.click()
    
    # Verify the presentation text is visible
    presentation_text = page.get_by_text("Present your work to the product owner during Sprint review")
    expect(presentation_text).to_be_visible()

    # Verify Sprint retrospective button text
    sprint_retrospective_text = page.get_by_text("End the sprint by evaluating your work in Sprint retrospective")




def test_sprint_retrospective_dialog(page: Page):
        page.goto("https://lejonmanen.github.io/agile-helper/")
        
        # Navigate to Sprint Retrospective
        button_locator = page.get_by_role("button")
        last_button = button_locator.get_by_text("Last")
        last_button.click()
        
        # Click Sprint Retrospective button
        sprint_retro_button = page.get_by_role("button").get_by_text("Sprint retrospective")
        sprint_retro_button.click()
        
        # Verify dialog content
        dialog = page.locator("dialog.sprint-ceremony")
        expect(dialog).to_be_visible()
        
        # Check heading
        heading = dialog.get_by_role("heading", level=2)
        expect(heading).to_have_text("Sprint retrospective")
        
        # Check list items
        list_items = dialog.locator("ol li")
        expect(list_items).to_have_count(3)
        expect(list_items.nth(0)).to_have_text("What should we start doing?")
        expect(list_items.nth(1)).to_have_text("What should we stop doing?")
        expect(list_items.nth(2)).to_have_text("What should we continue doing?")
        
        # Check complete button
        complete_button = dialog.get_by_role("button")
        expect(complete_button).to_have_text("The sprint is complete")