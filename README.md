
<div align="center">

# MARBLE MAYHEM

### My Hack Club Half Life Week 2 Project

**A colourful, modular, 3D-printable marble run inspired by MaBoRun**

<p>
  <img src="images/cad-assembly-preview.png" width="750" alt="Marble Mayhem CAD assembly">
</p>

**Designed using Onshape, FreeCAD and CAD reference components**

**Project Status:** CAD Prototype | Physical Testing Pending

</div>

---

## About This Project

For Week 2 of Hack Club Half Life, I decided to work on something completely different from my first week's project.

During Week 1, I worked on Starbie, my PCB-based digital pet project using KiCad. This week, I wanted to try something more mechanical and learn about 3D modelling.

The challenge was to design a marble run.

At first, I thought this would be pretty straightforward. I imagined making a few tracks, putting them together and letting a marble roll down.

It turns out there is a lot more to think about.

A marble run needs to have a continuous path, enough room for the marble to move, the correct slopes, strong supports and connections between all the different sections.

I also wanted the marble run to look interesting rather than just having one straight track.

That is how I came up with Marble Mayhem.

My idea was to create a colourful marble run with winding tracks, curves, a spiral, a funnel, a staircase-style section and a Plinko board.

One of the biggest challenges was keeping the design within the $30 Tier 1 budget.

I wanted a fairly complicated design, but I also needed to consider how much material it would take to actually print everything.

This project became a mixture of learning CAD, experimenting with different components, dealing with software problems and figuring out how a collection of parts could become a working marble run.

---

## The Idea Behind Marble Mayhem

I wanted Marble Mayhem to be more than a basic ramp.

My inspiration came from complicated marble-run toys that use different obstacles to change the direction and speed of the marble.

I especially liked the colourful MaBoRun designs with green rails, orange ramps, blue supports and large funnels.

The original idea was to have a marble start somewhere near the top, travel through several different obstacles and eventually reach a collection cup at the bottom.

Some of the features I wanted to include were:

- A large starting funnel.
- Long winding tracks.
- A spiral section.
- Curved and straight rails.
- A staircase-style track.
- A Plinko board with pegs.
- Support columns.
- A collection tray.
- A stable base.
- Connections between different track sections.

The goal was to make the path feel longer than the physical size of the model.

Instead of having the marble travel in a straight line, I wanted it to move around different parts of the structure.

I also wanted the design to be modular, meaning some sections could be changed or improved without needing to replace the entire marble run.

---

## My First Experience With Onshape

Before this project, I hadn't really used Onshape.

My previous Half Life project was made in KiCad, which is for circuit design, so switching to mechanical CAD was something new.

I started by following the Merbl guide:

https://github.com/karnxx/merbl/blob/main/guide.md

The guide explains how to create a marble run using Onshape and introduces several tools.

Some of the main CAD operations I learned about were:

**Sketch**

Sketching lets you create 2D shapes that can later become 3D objects.

**Dimension**

Dimensions are used to give shapes exact measurements instead of just drawing them by eye.

**Extrude**

Extrude turns a flat sketch into a 3D object by adding thickness or height.

**Sweep**

Sweep creates a 3D shape along a path. This is useful when designing curved tracks.

**Revolve**

Revolve turns a 2D profile around an axis. It is particularly useful for making funnels and circular components.

**Assembly**

An assembly brings separate components together and lets you position and connect them.

I started with simple shapes because I needed to understand the tools before working with more complicated curved designs.

One thing I learned pretty quickly was that something looking correct in 3D doesn't necessarily mean it will fit together with another part.

That became especially noticeable when I started connecting tracks.

---

## Starting With the Base

The first part I worked on was the base.

I originally considered using a solid square platform.

However, I realised that a large solid piece would use unnecessary printing material.

Because I had a limited budget, I experimented with making a hollow frame instead.

The basic idea was to create a large square and then draw a smaller square inside it.

After extruding the border, I had a lightweight frame.

<p align="center">
  <img src="images/base-onshape.png" width="700" alt="Initial base frame in Onshape">
</p>

This was one of my first proper attempts at editing sketches and working with dimensions.

It also introduced one of the main themes of this project: trying to make the design interesting without using unnecessary material.

The final assembly design uses a larger platform-style base to support the different components.

The early hollow frame remains part of my development process.

---

## Designing the Support Column

After experimenting with the base, I moved on to a support column.

This was a fairly simple part compared with the tracks.

I created a circle, extruded it into a cylinder and then experimented with removing material from the centre.

The idea was to create a hollow column rather than using a completely solid piece.

<p align="center">
  <img src="images/support-column-onshape.png" width="650" alt="Hollow support column">
</p>

The support columns are important because the marble run needs tracks at different heights.

Without proper supports, elevated tracks would have nothing holding them up.

Later designs also included a central support column near the winding tracks.

I had to consider where the supports were positioned because they could interfere with the path of the marble.

I learned that supports are not just decorative.

They affect the stability, spacing and overall structure of the project.

---

## Creating the Straight Track

The straight track was one of the first actual marble-run components I worked on.

I started with a rectangular base and then added raised walls along both sides.

This created a U-shaped channel.

<p align="center">
  <img src="images/straight-track-onshape.png" width="700" alt="Straight marble track">
</p>

The reason for adding walls is fairly obvious: without them, the marble could roll off the sides.

However, the width of the track matters.

If the channel is too narrow, the marble might get stuck.

If the walls are too low, the marble could fall out on a curve.

I also had to think about how this straight section would connect to other tracks.

At first, I was mainly focused on making the shape itself.

Later, I realised that the ends of the track were just as important as the middle.

A straight track that cannot connect properly to another track isn't very useful in a modular marble run.

---

## Designing the Curved Track

The curved track was more complicated.

Instead of making a basic rectangle, I had to work with arcs and curved shapes.

The idea was to create a channel that would allow the marble to change direction smoothly.

<p align="center">
  <img src="images/curved-track-onshape.png" width="700" alt="Curved marble track">
</p>

I had to consider the inner and outer edges of the curve and make sure the channel had enough width for the marble.

I also learned that curved tracks can look correct from one angle but have problems when you connect them to straight sections.

When I tried connecting my straight and curved tracks in Onshape, the parts initially overlapped.

I experimented with Fastened mates and different connector positions.

Getting the pieces into approximately the right position was possible, but making the channel surfaces line up correctly was harder.

That experience showed me why CAD assembly tools are important.

It is not enough to have two objects touching.

The marble needs a smooth path between them.

---

## Working With Assemblies

Once I had some basic parts, I started learning about assemblies.

In Onshape, I created different Part Studio tabs for components such as the support column, straight track and curved track.

I then used an Assembly tab to bring pieces together.

At first, I wasn't sure how to use Fastened mates.

I had to learn how mate connectors work and how they determine the position and orientation of different parts.

One of the problems I ran into was selecting the wrong position on a track.

That caused pieces to overlap instead of joining end-to-end.

I also noticed that two tracks could be connected in the assembly while their walls still didn't line up properly.

This was a useful lesson because I had assumed that if Onshape attached two components, the connection would automatically be correct.

It doesn't work like that.

The connection still needs to be checked from different angles.

---

## Moving Towards a More Complicated Marble Run

After working with the basic components, I wanted to develop the project into something much more interesting.

I used CAD reference components and assisted modelling to explore more complicated layouts inspired by MaBoRun.

The assembly went through several different versions.

Some versions had circular tracks around a central tower.

Others had more complicated curved rails, funnels, supports and obstacles.

<p align="center">
  <img src="images/earlier-cad-preview.png" width="750" alt="Earlier CAD assembly concept">
</p>

One of the problems with the earlier layouts was that some tracks looked connected from a distance but were actually separate.

This made the model look more complete than it really was.

I started paying more attention to the actual route a marble would follow.

For a marble run to work, the track sections need to connect correctly, the marble must be able to move downhill, and supports must not block the route.

The more complicated the model became, the more important those details were.

---

## The Colourful Design

I wanted Marble Mayhem to stand out visually.

Instead of using the same colour for every component, I chose a colourful design inspired by MaBoRun.

The main colours are:

| Colour | Components |
|---|---|
| Orange | Funnel, ramps, staircase sections and supports |
| Green | Winding rails, curved tracks and spiral |
| Blue | Support pillars and supporting track structures |
| Black | Main base |

The colour choices help distinguish different areas of the design.

They also make the model easier to understand when looking at the full assembly.

For example, the green components mainly show the marble paths, while the blue and orange structures help support or redirect the marble.

The final colours will depend on the filament available when the parts are printed.

---

## The Funnel

One of the main features of the design is the funnel.

The funnel is intended to act as a starting point or transition between track sections.

A marble enters the wider circular area, moves towards the centre and exits through an opening.

I liked the idea of using a funnel because it introduces another type of motion instead of having the marble travel only through straight channels.

The funnel also makes the overall marble run look more interesting.

However, creating a funnel shape is only part of the challenge.

The exit needs to connect to another track at the right height.

If the exit is too far away from the next section, the marble may fall outside the track.

This is one of the areas that still needs proper testing.

---

## The Spiral

The spiral is another major part of Marble Mayhem.

The goal of the spiral is to make the marble travel a longer distance while taking up a relatively small amount of space.

The track winds around a central area and gradually descends.

This makes the route longer without needing a massive base.

The spiral also needs supports.

If the track is elevated too far without support, it may be unstable after printing.

One of the later design changes involved adding a central support column near the spiral.

The column helps define the structure of that part of the marble run.

I also had to consider whether the spiral had enough clearance for the marble.

A winding track with tight curves can create more opportunities for the marble to get stuck.

---

## The Staircase Section

I wanted to include a staircase-style section because it looks completely different from a normal ramp.

The reference MaBoRun design uses a mechanical staircase arrangement.

My CAD prototype uses a simplified fixed structure rather than recreating the manufacturer's motorised mechanism.

The staircase section is intended to redirect the marble through a stepped or channelled descent.

This is something that needs to be checked carefully during physical testing.

I cannot assume that a marble will travel correctly over every step just because the model looks good on screen.

The step dimensions and transitions may need adjustment before printing the final version.

---

## The Plinko Board

One of my favourite ideas for the marble run was including a Plinko board.

Plinko uses a series of pegs or obstacles that cause a falling ball to change direction.

I wanted to include this because it makes the marble's movement less predictable.

Instead of following exactly the same path through a smooth channel, the marble can bounce between different pegs.

The Plinko board needs:

- A clear entrance.
- Enough space between the pegs.
- Side walls to stop the marble from escaping.
- A downward slope or suitable orientation.
- A collection area at the bottom.
- An exit that connects to the remaining route.

The peg spacing is especially important.

If the gaps are too small, the marble might get trapped.

If the pegs are too far apart, the obstacle becomes less interesting.

The current Plinko section is part of the CAD prototype and still needs physical testing.

---

## The Final Assembly

The latest design brings together several different track and obstacle sections.

<p align="center">
  <img src="images/cad-assembly-preview.png" width="800" alt="Marble Mayhem final CAD prototype">
</p>

The model includes the colourful components I wanted, including the large funnel, winding green rails, orange obstacles, blue support structures and black base.

The design has also been revised to improve the continuity of the marble path.

However, I want to be clear about the project status.

This is currently a CAD prototype.

I have not yet demonstrated that a real marble can travel through the complete model without getting stuck.

The STEP and STL files provide a starting point for manufacturing and testing, but they do not prove that the entire marble run works.

The next major stage is physical printing and testing.

---

## Using FreeCAD

One unexpected problem was that the larger STEP assemblies became difficult to import into Onshape.

I repeatedly encountered a message saying that the memory limit had been exceeded.

The smaller beginner-level parts opened normally, but the complicated assembly caused problems during translation.

Because of that, I decided to try FreeCAD.

FreeCAD is a free CAD application that runs directly on my Mac.

Unlike Onshape, it opens CAD models locally.

That means it uses my computer's resources instead of relying on a cloud importer.

I installed the Intel version because my Mac uses an Intel Core i5 processor.

I then experimented with importing the STEP model and adjusting the import settings.

This introduced another CAD program into the project.

It also taught me that a file working in one CAD application doesn't necessarily mean another application will handle it in the same way.

Large assemblies can become difficult to process, particularly when they contain many detailed surfaces.

---

## STEP Files vs STL Files

One thing I learned during the project was the difference between STEP and STL files.

### STEP

STEP files are commonly used for exchanging 3D CAD geometry between applications.

I used STEP files to work with component geometry and assembled models.

STEP is generally more useful when importing parts into a CAD application for further engineering work.

### STL

STL files describe 3D surfaces using triangles.

They are commonly used in 3D-printing workflows.

STL files are useful when preparing individual components for slicing and printing.

However, simply having an STL does not guarantee that a part will print successfully.

Wall thickness, overhangs, supports, orientation and printer settings still matter.

### FreeCAD project files

FreeCAD uses `.FCStd` files for its own documents.

These can preserve a FreeCAD project for further work.

Imported STEP objects do not automatically become native parametric features with their original modelling history.

---

## Budget Planning

For this challenge, I am working with a Tier 1 budget limit of $30.

That budget is one of the main constraints of the project.

A complicated marble run could become expensive to manufacture, especially if it uses a large amount of plastic.

I have been considering several ways to reduce the cost.

### Material-saving ideas

**Hollow supports**

Where suitable, hollow supports can use less material than completely solid columns.

**Thin track walls**

Track walls should be strong enough to contain the marble without being unnecessarily thick.

**Modular components**

Separating the design into modules can make it easier to replace or improve individual pieces.

**Lightweight base**

A hollow frame or ribbed base may use less material than a thick solid platform.

**School 3D printer**

I am considering using my school's 3D printer, depending on availability and permission.

This could reduce the cost compared with using an external printing service.

### Budget status

| Item | Status |
|---|---|
| CAD design | Prototype available |
| Printing material | To be confirmed |
| Printer access | School printing planned |
| Marble | Size and cost to confirm |
| Extra hardware | Depends on final assembly |
| Total manufacturing cost | Not yet verified |

I am not claiming the project fits under $30 until the printing costs and required materials have been checked.

---

## Physical Printing Plan

The next step is to turn the CAD model into physical components.

Before printing everything, I want to test the parts most likely to cause problems.

The main things that need testing are:

1. Whether the selected marble fits inside the tracks.
2. Whether the marble moves smoothly through curved sections.
3. Whether the funnel correctly releases the marble.
4. Whether the track joints align.
5. Whether the Plinko pegs have enough clearance.
6. Whether the central support structure is stable.
7. Whether the staircase section works as intended.
8. Whether the assembled base can support all the components.

It would be a waste of filament to print the entire model before checking these details.

A better approach is to print a small selection of components first.

If those parts work, I can continue with the rest.

If they don't, the CAD files can be adjusted before more material is used.

---

## Problems I Encountered

This project involved several different challenges.

### 1. Learning a new CAD program

I wasn't familiar with Onshape when I started.

Understanding sketches, extrusions, dimensions, faces and planes took practice.

### 2. Making curved tracks

Straight tracks were relatively simple.

Curved tracks required more attention to arcs, channel width and wall geometry.

### 3. Connecting components

The assembly tools initially confused me.

Selecting the wrong mate connectors caused the parts to overlap.

Even after positioning them, some joints needed additional adjustments.

### 4. Designing something complicated

I wanted the project to look like an advanced marble run.

That made the CAD much more complex than the beginner parts I started with.

### 5. Finding disconnected sections

Some earlier CAD reference assemblies looked complete but contained disconnected paths.

I had to consider how a marble would actually move between different obstacles.

### 6. Software memory limits

Onshape struggled to import the larger STEP assembly.

This led me to experiment with FreeCAD as an alternative.

### 7. The budget

The design needed to balance appearance, complexity and material usage.

I still need to verify the final physical printing cost.

---

## What I Learned

I learned quite a lot from this project, even though the marble run has not yet been physically tested.

The biggest lesson was that a 3D model and a working mechanical design are not the same thing.

Something can look impressive on screen but still have problems with its geometry.

For a marble run, small issues can have a big effect.

A slightly misaligned connection could stop a marble.

A support column in the wrong location could block the track.

An incorrectly sloped section could prevent the marble from moving.

I also learned that CAD software can handle the same files differently.

Onshape was useful for learning basic modelling and assemblies.

FreeCAD gave me another way to inspect larger STEP models.

I also became more familiar with how different 3D-printing file formats are used.

Most importantly, I now understand why physical testing matters.

CAD is a useful way to plan the design, but real-world testing is needed to see whether it actually works.

---

## Project Files

The repository is intended to include the following files and folders.

```text
HalfLife-Project-Week-2/
|
|-- README.md
|
|-- images/
|   |-- base-onshape.png
|   |-- support-column-onshape.png
|   |-- straight-track-onshape.png
|   |-- curved-track-onshape.png
|   |-- earlier-cad-preview.png
|   |-- cad-assembly-preview.png
|
|-- CAD/
|   |-- Marble_Mayhem_V2_assembled.step
|   |-- individual-component-files.step
|
|-- STL/
|   |-- individual-printable-parts.stl
|
|-- BOM.csv
|
|-- JOURNAL.md
```

This is the planned repository structure. Some files may be added or renamed as the project progresses.

---

## About the CAD Reference Models

Some of the more complicated CAD components in this project were generated or provided with assistance rather than modelled entirely by hand.

I used these components as references while exploring how to create a more complicated marble-run assembly.

My initial hands-on Onshape work focused on learning the software and creating simpler parts such as the base, support column, straight track and curved track.

The later assemblies helped me explore more complicated shapes and identify issues such as disconnected paths and overly complex imported geometry.

I want to keep that distinction clear because the project includes both my own early modelling practice and externally assisted CAD components.

My main focus now is testing, improving and preparing the design for manufacturing.

---

## Things I Still Need to Do

There are several tasks remaining before I can call the marble run finished.

- [ ] Confirm access to a suitable 3D printer.
- [ ] Confirm the marble diameter.
- [ ] Check the track clearances.
- [ ] Verify the printing cost.
- [ ] Slice the individual parts.
- [ ] Print small test components.
- [ ] Test the track connections.
- [ ] Check the funnel exit.
- [ ] Test the spiral section.
- [ ] Test the Plinko board.
- [ ] Check the staircase movement.
- [ ] Print the remaining components.
- [ ] Assemble the physical marble run.
- [ ] Test the complete marble route.
- [ ] Photograph the finished build.

These tasks will help determine which parts of the prototype need further changes.

---

## Future Improvements

Once I have a physically working version, there are several things I would like to improve.

### Better modular connectors

I would like to develop more reliable connections so parts can be removed and replaced easily.

### Longer marble paths

I want to experiment with creating additional track sections that make the marble travel farther.

### More obstacles

A more advanced version could include extra funnels, switches or alternative routes.

### Improved supports

I would like to make the supports lighter while keeping the structure stable.

### Material optimisation

After testing, I could adjust wall thicknesses and printing orientation to reduce material usage.

### Better assembly instructions

I want to document how each component fits together so the marble run is easier to assemble.

### Mechanical features

The MaBoRun inspiration includes moving mechanisms.

A future version could explore a working marble elevator or other powered feature.

This would be a separate design challenge because it introduces moving parts and additional mechanical requirements.

---

## Final Thoughts

Marble Mayhem has been a very different experience from my Week 1 Starbie PCB project.

With Starbie, I was learning electronics design.

With Marble Mayhem, I've been learning how to think about physical shapes, mechanical connections, materials and movement.

I originally expected a marble run to be a fairly simple project.

I quickly realised that designing one properly involves a surprising amount of planning.

The most frustrating part has probably been dealing with track connections and the large CAD files.

It is annoying when a model looks good but doesn't behave the way you expected.

However, those problems also helped me understand what needs to be checked before something can actually be built.

I'm happy with the overall direction of the design, especially the colourful tracks and different obstacle sections.

At the same time, I know the project isn't finished just because the CAD model exists.

The next big step is testing the design with a real marble and making whatever changes are needed to get everything moving properly.

I'm interested to see how much of the design works on the first attempt and what will need to be changed.

Either way, this project has given me a much better introduction to mechanical CAD and 3D printing.

---

<div align="center">

### Marble Mayhem

**Hack Club Half Life — Week 2**

Designed as a CAD prototype with future 3D printing and testing planned.

**Built to experiment, learn and improve.**

</div>
