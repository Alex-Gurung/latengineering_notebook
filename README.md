# Template Engineering Notebook
Engineering notebook (template by FTC Team 12787 Fools Team Ahead)

## What Do I Have to Do Again?
### Daily updates
#### Folder hasn't been created yet:
* Manual Method: 
    * make a new folder under _src/engineering/_ with the day in **year.month.day** format
        * Each day directory has four things:
            * Day file
                * In **year.month.day.tex** format
                * Should have title, table, notes, updates, tags
            * Notes file
                * In **notes.tex** format
                * Details general notes for the day, any pictures, etc
                * Basically stuff that doesn't fit in a short reflections thing 
            * Updates file
                * In **updates.tex** format
                * Any import systems updates should go here
                * For example, if we completed the relic system or finished an autonomous program, make note of it
            * Tags file
                * In **tags.tex** format
                * Look below for acceptable tags (list is flexible but let everyone know if you change it)
                * Helps us track progression of specific systems that were worked on, and for the judges we can point to what days each system was worked on 
* Quicker (but still manual) Alternative:
    * copy and paste, make necessary changes
    * Things that need to be changed:
        * **year.month.day/** directory name
        * **year.month.day.tex** file name (within that directory)
            * Also within it the table should be cleared (see below) and the section title updated
        * Empty **notes.tex**, **updates.tex**, **tags.tex**
        * **name_year.month.day/** directory name
            * Empty that directory
* **_<span style="color:#e0165b">AUTOMATED</span>_** : Recommended (and easiest) method
    * From the base directory (one up from _src/_)
    * Run _create_day.exe_
        * Fill in the prompts, make sure to follow the format prescribed
#### Adding Your Reflections/Updates
* Manual Method:
    * Go to the appropriate directory, something along the lines of _src/engineering/year.month.day/_
    * Add any notes to **notes.tex**, tags to **tags.tex**, and updates to **updates.tex**
    * Go to the _name\_year.month.day_ directory and add a **{{name}}_year.month.day.tex** file ({{name}} is your name)
        * Fill that file with your reflections, plain text will work, but if you want fancier formatting latex will work too
    * Go back to the _year.month.day_ directory and edit **year.month.day.tex**
        * In the table, add a row for your name and in the reflections column put `\input{src/engineering/year.month.day/name_year.month.day/{{name}}_year.month.day` in place of _"What I Did"_
        * See below for table specifics
* **_<span style="color:#e0165b">AUTOMATED</span>_** : Recommended (and easiest) method
    * From the base directory (one up from _src/_)
    * Run _add_reflections.exe_
        * Fill in the prompts, make sure to follow the format prescribed
### Tables, How Do They Work?
Here's a sample table:
```
\begin{center}
    \begin{tabular}{ |p{2cm}|p{10cm}| }
        \hline
        \textbf{Name} & \textbf{What We Did/Reflections} \\
        \hline
        Eric & \textit{What I Did} \\
        \hline 
        John & \textit{What I Did} \\
        \hline 
        Kieran & \textit{\input{src/engineering/2017.09.23/name_2017.09.23/kieran_2017.09.23}} \\
        \hline 
        Jacques & \textit{What I Did} \\
        \hline 
        William & \textit{What I Did} \\
        \hline 
        Alex & \textit{\input{src/engineering/2017.09.23/name_2017.09.23/alex_2017.09.23}} \\
        \hline 
        Mansi & \textit{What I Did} \\
        \hline
    \end{tabular}
\end{center}
```
What does it all do?
* `\begin{center}`
    * Centers the table
* `\begin{tabular}{ |p{2cm}|p{10cm}| }`
    * Creates a table with a 2cm column and a 10cm column
    * If you want more columns, add more |p{width}| sections
    * If you want more rows, add more of the lines
    * You can change the respective width of the columns by editing the {2cm} or {10cm} sections, but these widths have worked so far for us
* `\hline`
    * Creates a row separator (a line separating two rows), not needed for a row to exist but good for formatting
* `\textbf{Name} & \textbf{What We Did/Reflections} \\`
    * Does a lot of things, let's split it up
    * `\textbf{Name}`
        * Sets the first column to be a bolded **Name**
    * ` & `
        * Marker that allows LaTex to split up the columns (& goes between each column)
    * `\textbf{What We Did/Reflections}`
        * Same as with the **Name** but with **What We Did/Reflections**
    * `\\`
        * Defines the end of a row, also used in text to force a new line (not recommended for that purpose)
## Repo Organisation
* _src/_ 
    * Contains actual content of notebook
    * _cover/_
        * Contains the cover page and any unique, initial pages that we need
    * _engineering/_
        * The content of the _Engineering Section_ of the notebook
        * (Robot related parts of team)
    * _images/_
        * place to store any images you want to put in the notebook
    * _mentors/_
        * If you have mentors put any relevant info. here!
    * _outreach/_
        * Any outreach events or programs
    * _team/_
        * includes information about the team
    * _tools_
        * If you want to highlight any tools put them in here and reference them in the _tools.tex_ file
* _main.tex_
    * LaTex file you actually compile, pulls info. from all of the other sections in _src/_

## Daily Update Organisation
Daily updates are done in their respective sub-folders

## Tag formatting
Comma separated, use allowed set (ask group for changing set)

### Sample Tags
* Chassis
* Autonomous
* Autonomous-*
    * Autonomous related
* Teleop
* Teleop-*
    * Teleop related
* Relic
* Glyph
* Jewels
* Outreach
* Brainstorm
* Field
