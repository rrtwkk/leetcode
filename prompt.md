# README Update Prompt Template

Use this template to update the README.md file when new files are added to the project. Replace the placeholders with actual information.

## Basic Structure
```markdown
# LeetCode Solutions

This repository contains solutions to various LeetCode problems implemented in different programming languages.

## [Programming Language]

The `[language]` directory contains solutions implemented in [Language Name]. [Brief description of the language].

### Key Features of [Language]
- [Feature 1]
- [Feature 2]
- [Feature 3]
- [Feature 4]
- [Feature 5]

### Common [Language] Libraries and Built-in Modules Used
- [Library/Module 1]: [Brief description]
- [Library/Module 2]: [Brief description]
- [Library/Module 3]: [Brief description]
- [Standard data structures and functions]
- [Other relevant features]

### [Language] Best Practices
1. [Best Practice 1]
2. [Best Practice 2]
3. [Best Practice 3]
4. [Best Practice 4]
5. [Best Practice 5]

### Running [Language] Code
```[language]
# Basic [Language] file execution
[command to run file]

# Using [Language] interactive shell/REPL
[command to start interactive shell]
```

### Development Environment
- [Language Version]
- [Recommended IDEs/Editors]
- [Additional tools or requirements]
```

## Instructions for Use

1. **Analyzing New Files**
   - Scan the new files for:
     - Imported libraries and modules
     - Data structures used
     - Programming patterns
     - Language-specific features

2. **Updating README.md**
   - If adding a new language:
     - Create a new section following the template
     - Include language-specific information
   - If adding to existing language:
     - Update the "Common Libraries" section if new libraries are used
     - Add any new best practices discovered
     - Update development environment if needed

3. **Maintaining Consistency**
   - Keep the same format across all language sections
   - Use consistent heading levels
   - Maintain similar level of detail for each section

4. **Code Examples**
   - Include basic examples of running code
   - Show common patterns used in the solutions
   - Demonstrate language-specific features

## Example Update Process

1. When new files are added:
   ```
   @/[language] 
   File structure of this repo would be:
   [programming language]: It contains code in [language] language.
   eg:
   [language]: It contains code in [language] language.

   Scan files under the [programming language] folder and Update README.md file in markdown format with below details:
   1. Look for any inbuilt imports I have used or programming library I have used.
   2. Write few lines of blurb about it, eg how to use it, what is the use of it, etc.
   ```

2. The assistant will:
   - Analyze the new files
   - Update the README.md following the template
   - Maintain consistency with existing content
   - Add any new relevant information

## Notes
- Keep the README.md focused on language features and best practices
- Avoid solution-specific details
- Update the development environment section when new tools are required
- Maintain a clean and organized structure 