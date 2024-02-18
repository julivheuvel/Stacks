# CSS Library powered by Sass


<summary>Table of Contents</summary>
    <ul>
        <li><a href="#about-the-project">About The Project</a></li>
        <li><a href="#documentation">Documentation</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>

<details>
<summary>Documentaion</summary>
    <ol>
        <li>
            <a href="#utilities">Utilities</a>
        </li>
        <li>
            <a href="#components">Components</a>
        </li>
    </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
    This personal library is a frontend toolkit built utilizing Syntactically Awesome Style Sheets

    Architecture:
    Describe the overall architecture and organization of your CSS library.
    Explain how the library is structured, including directories for stylesheets, partials, mixins, functions, variables, and any other relevant components.

    Features:
    Detail the features and components included in your CSS library, such as:
    Base styles: Reset styles, typography settings, and global styles.
    Components: Reusable UI components like buttons, forms, cards, and navigation.
    Layouts: Grid systems, flexbox helpers, and responsive layout utilities.
    Utilities: Helper classes and mixins for common tasks like spacing, colors, and text manipulation.
    Theming: Variables and mixins for easy theming and customization.
    Transitions and animations: Predefined animations and transitions to enhance user experience.
    Accessibility: Guidelines and utilities for building accessible UI components.

    Examples and Demos:
    Showcase real-world examples and demos illustrating how your CSS library can be used to style different types of web interfaces.
    Provide live demos or screenshots to showcase the appearance and functionality of various 

    
<p align="right">(<a href="#css-library-powered-by-sass">back to top</a>)</p>


<!-- Documentation -->
## Documentation
<details>
    <summary>Table of Contents</summary>
        <ol>
            <li>
                <a href="#base-styles">Base Styles</a>
            </li>
            <li>
                <a href="#components">Components</a>
            </li>
            <li>
                <a href="#forms">Forms</a>
            </li>
            <li>
                <a href="#layout">Layout</a>
            </li>
            <li>
                <a href="#utilities">Utilities</a>
            </li>
        </ol>
</details>

### Base Styles
<details>
    <summary>Contents</summary>
        <ul>
            <li>
                <a href="#resets">Resets</a>
            </li>
        </ul>
</details>

#### Resets
Resets borders and margins to 0. Sets box-sizing to border box
    typography settings
    global setings

<p align="right">(<a href="#documentation">back to documentation</a>)</p>


### Components

<details>
    <summary>Contents</summary>
        <ul>
            <li>
                <a href="#accordian">Accordian</a>
            </li>
        </ul>
</details>

#### Accordion

    alerts
    badge
    breadcrumb
    buttons
    button-group
    card
    carousel
    close button
    collapse
    dropdowns
    list group
    modal
    navbar
    navs, tabs
    offcanvas
    pagination
    placeholders
    popovers
    progress
    srcollspy
    spinners
    toasts

<p align="right">(<a href="#documentation">back to documentation</a>)</p>


### Forms
    overview
    form-control
    select
    checks & radios
    range
    input group
    floating labels
    layout
    validation

<p align="right">(<a href="#documentation">back to documentation</a>)</p>


### Layout
<details>
    <summary>Contents</summary>
        <ul>
            <li>
                <a href="#breakpoints">Breakpoints</a>
            </li>
            <li>
                <a href="#containers">Containers</a>
            </li>
            <li>
                <a href="#grid">Grid</a>
            </li>
            <li>
                <a href="#columns">Columns</a>
            </li>
            <li>
                <a href="#gutters">Gutters</a>
            </li>
        </ul>
</details>

#### Breakpoints
Predefined breakpoints include:
    <ul>
        <li>0</li>
        <li>200</li>
        <li>400</li>
        <li>800</li>
        <li>1000</li>
        <li>1200</li>
        <li>1600</li>
        <li>2000</li>
    </ul>
Classes created include:
| class name |  behavior | 
| :--------: | :-------: |
| .re-text   | font size |


#### Containers
#### Grid
#### Columns
#### Gutters

<p align="right">(<a href="#documentation">back to documentation</a>)</p>


### Utilities
<details>
    <summary>Contents</summary>
        <ul>
            <li>
                <a href="#background">Background</a>
            </li>
            <li>
                <a href="#borders">Borders</a>
            </li>
            <li>
                <a href="#colors">Colors</a>
            </li>
            <li>
                <a href="#display">Display</a>
            </li>
            <li>
                <a href="#flex">Flex</a>
            </li>
            <li>
                <a href="#float">Float</a>
            </li>
            <li>
                <a href="#height">Height</a>
            </li>
            <li>
                <a href="#interactions">Interactions</a>
            </li>
            <li>
                <a href="#link">Link</a>
            </li>
            <li>
                <a href="#object-fit">Object-fit</a>
            </li>
            <li>
                <a href="#opacity">Opacity</a>
            </li>
            <li>
                <a href="#Overflow">Overflow</a>
            </li>
            <li>
                <a href="#Position">Position</a>
            </li>
            <li>
                <a href="#Shadows">Shadows</a>
            </li>
            <li>
                <a href="#Sizing">Sizing</a>
            </li>
            <li>
                <a href="#Spacing">Spacing</a>
            </li>
            <li>
                <a href="#Tables">Tables</a>
            </li>
            <li>
                <a href="#text">Text</a>
            </li>
            <li>
                <a href="#Vertical-align">Vertical align</a>
            </li>
            <li>
                <a href="#Visibility">Visibility</a>
            </li>
            <li>
                <a href="#width">Width</a>
            </li>
            <li>
                <a href="#Z-Index">Z-Index</a>
            </li>
        </ul>
</details>



#### Background
Customize background with colors. All predefined css colors can be called with the class prefix `.bg-colorName`and can append tint or shade variation followed by degree of shade defined by 1-9 representing 10% intervals. Opacity of bg color can be defined on the base color by appending `-op-%` from 1%-99%

| background    |  class name               | 
| :-----------: | :-----------------------: |
| base colors   | .bg-{colorName}           |
| bg opacity    | .bg-{colorName}-op-{%}    |
| tinted colors | .bg-{colorName}-light-{#} |
| shaded colors | .bg-{colorName}-dark-{#}  |

<p align="right">(<a href="#documentation">back to documentation</a>)</p>


#### Borders
#### Colors
#### Display
#### Flex
#### Float

#### Height
Customizing with height can be defined by either `.h` or `.vh` and appended by a value ranging from 1 through 200. Default unit for `.h` will be in % unless otherwise defined directly after value, i.e. `.h-10px`

| height                |  class name           | 
| :-------------------: | :-------------------: |
| base                  | .h-{value}            |
| base max              | .h-{value}-max        |
| base min              | .h-{value}-min        |
| base with unit        | .h-{value}{unit}      |
| base with unit max    | .h-{value}{unit}-max  |
| base with unit min    | .h-{value}{unit}-min  |
| vh base               | .vh-{value}           |
| vh base max           | .vh-{value}-max       |
| vh base min           | .vh-{value}-min       |

<p align="right">(<a href="#documentation">back to documentation</a>)</p>

#### Interations
#### Link
#### Object-fit
#### Opacity
#### Overflow
#### Position
#### Shadows
#### Sizing
#### Spacing
#### Tables

#### Width
Customizing with width can be defined by either `.w` or `.vw` and appended by a value ranging from 1 through 200. Default unit for `.w` will be in % unless otherwise defined directly after value, i.e. `.w-10px`

| width                |  class name           | 
| :-------------------: | :-------------------: |
| base                  | .w-{value}            |
| base max              | .w-{value}-max        |
| base min              | .w-{value}-min        |
| base with unit        | .w-{value}{unit}      |
| base with unit max    | .w-{value}{unit}-max  |
| base with unit min    | .w-{value}{unit}-min  |
| vw base               | .vw-{value}           |
| vw base max           | .vw-{value}-max       |
| vw base min           | .vw-{value}-min       |

<p align="right">(<a href="#documentation">back to documentation</a>)</p>

#### Text
Customize text with colors. All predefined css colors can be called with the class prefix `.t-colorName`and can append tint or shade variation followed by degree of shade defined by 1-9 representing 10% intervals. Opacity of text color can be defined on the base color by appending `-op-%` from 1%-99%

| text          |  class name              | 
| :-----------: | :----------------------: |
| base colors   | .t-{colorName}           |
| text opacity  | .t-{colorName}-op-{%}    |
| tinted colors | .t-{colorName}-light-{#} |
| shaded colors | .t-{colorName}-dark-{#}  |

Text Align
| text      |  class name      | 
| :-------: | :--------------: |
| start     | .t-align-start   |
| end       | .t-align-end     |
| center    | .t-align-center  |
| justify   | .t-align-justify |

Text Wrap
| text     |  class name     | 
| :------: | :-------------: |
| wrap     | .t-wrap-wrap    |
| nowrap   | .t-wrap-nowrap  |
| balance  | .t-wrap-balance |
| pretty   | .t-wrap-pretty  |
| stable   | .t-wrap-stable  |

<p align="right">(<a href="#documentation">back to documentation</a>)</p>

#### Vertical align
#### Visibility
#### Z-Index

<p align="right">(<a href="#documentation">back to documentation</a>)</p>

<p align="right">(<a href="#css-library-powered-by-sass">back to top</a>)</p>






<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#css-library-powered-by-sass">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Juli Vanden Heuvel - [email](juli.heuvel@gmail.com)

Project Link: [Library](https://github.com/julivheuvel/Stacks/tree/main/Java_Jingles)

<p align="right">(<a href="#css-library-powered-by-sass">back to top</a>)</p>