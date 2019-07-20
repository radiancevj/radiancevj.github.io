Title: History of Radiance
Date: 2019-07-18
Tags: lights, code
Author: Eric Van Albert
Illustration: rush-2016.jpg

## The 2012 East Side Party

The annual East Side Party that welcomes new students to MIT
was going to happen at the end of August, and I wanted to put on a light show.
I had my first college internship at Fitbit in the summer of 2012,
along with some friends from MIT.
One of them got put on a plane to China and came back with
a suitcase full of RGB LED strips.
I spent many long nights at the office
soldering together the custom hardware to run the lights.

Ultimately, the software stack that ran the light show looked like this:
![Light output pipeline, involving Mixxx, custom hardware, and seq24]({attach}seq24-workflow.png)

The lights were not commanded directly. Instead,
MIDI signals would tell control boards to send pulses of different colors
down the LED strip, or to flash the entire strip one color.
A bare-bones sequencer called [seq24](http://www.filter24.org/seq24/) was used to "VJ" the show,
with help from a MIDI keyboard. seq24 took MIDI clock information
from [Mixxx](https://mixxx.org/), a free piece of DJ software.

![The East Side Party, 2012]({attach}rush-2012.jpg)

Looking back, the party went very well.
The light patterns were primitive, but the audio synchronization
and expressiveness of the display was inspiring.
Those features have (hopefully) persisted through seven years
of writing, throwing out, and rewriting light control software.

## Sequencing

Writing a better sequencer was the next task.
It did manual beat syncing (the intent was to eventually make it automatic.)
You can "play" patterns using the keyboard, as well as record sequences.
I honestly don't know how to use it anymore, it had a very arcane keyboard interface.
The output was still MIDI clock + MIDI notes for patterns.

![Light output sequencer written in pygame]({attach}python-1d.png)

This project was called "[beat-off](https://github.com/ervanalb/beat-off/tree/python-1d)"
(yes, it was a masturbation joke)
and this code eventually turned into Radiance.

## Livecoding

While I could tolerate this crappy GUI,
my partner-in-crime Zach was born on and will die on the command line.
He was convinced that the best sequencer was `vim` with
a little bit of Python code to help out.
This led to "[cursedlight](https://github.com/zbanks/cursedlight)"
(lovingly pronounced "curse delight")
the third generation of light control software.
It saw some use in a set at Steer Roast 2014.

!()[]

On the surface, it doesn't seem to bear much resemblance to
Radiance today, but the mentality and aesthetic of livecoding lives on.
Zach and I aren't artists, and of all the interfaces we had tried
up to this point, a terminal was the most expressive for us.
It definitely had its shortcomings, but helped to highlight what was missing.
It also seems to be the first place where we used a planar canvas with
LED strips mapped across it.

## Control Issues

Version four is where Radiance finally started looking a little bit like how it does today.
You can clearly the workflow of
compositing a set of patterns,
setting up a deck of patterns,
compositing them onto a 2D square,
and sampling across it to light LED strips.
There's even a waveform display with automatic beat tracking.
The other thing you can clearly see is that it looks way more like an industrial control panel
than VJ software.
There are 40 knobs spread over 8 patterns controlling things like "rho" and "angle k".
Some sliders were inputs and some were outputs, and you could connect them together.
That's why there's a filter bank in the top right: you could connect the "onset detection function"
to "automatic gain control", and connect the output of that to the "radius" of one of the circle patterns.
That's how you make a ball that bounces to the beat.

![Colorful UI with sliders everywhere]({attach}control-overload.png)

It was very cool that such connections were possible, but impractical from a performance perspective.
If a song comes on that warrants a bouncing ball, you don't want to have to think about AGCs and
ODFs. Even with all of these knobs, we still had to kludge in the idea of
"color palettes," since it was hard to express color with a 1D slider.
Despite having so many features, the biggest takeaway was what *not* to do:
don't have too many knobs.

## Function composition

Up until this point, we hadn't been using any sort of graphics acceleration.
The last version was pushing the limits of CPU rendering,
so we decided to pull in OpenGL and write effects as shaders.

This version was the first to have effects "chains", where an effect modifies the video coming into it.
The previous version simply alpha-composited effects; this version behaved more like function composition.
It's also the first place you'll find the "one slider per pattern" paradigm.
Both of these are key parts of Radiance today.

The main limitation of this version was that only four patterns could be chained.
It was set up very much like a DJ deck, so that two decks of four patterns each would be mixed together using alpha-compositing.
This wound up being powerful enough to demonstrate the potential of compositional patterns, but limiting enough to be quite frustrating while performing.

![Radiance crossed with a DJ app]({attach}radiance-sdl.png)

This version was used to run the lights at the
2016 East Side party. Zach and I had both graduated, but were able to help
a team of three undergrads set up the light show using the newly-renamed "Radiance."
This was a real milestone because it was the first time our software
had been used seriously by people who didn't develop it.
It was also probably the first light show that outdid the original in 2012.

<video muted autoplay loop>
<source src="{attach}rush-2016.mp4" type="video/mp4">
</video>

## The finishing touches

Around the time of the East Side party, it became clear that
Radiance could do more than just lights.
It also became clear that it needed a real user interface.
This version marks the last full rewrite of the codebase.

<video muted autoplay loop>
<source src="{attach}radiance-2017.mp4" type="video/mp4">
</video>

This version introduced multi-input patterns,
the venerable `uvmap`,
image input, video input, and free-form graph topology.
After great debate, we decided to break our one-slider rule
and add a frequency adjustment to every effect.
It is also the first version to target screen / projector output.
We recently brought back the ability to livecode effects.

<video muted autoplay loop>
<source src="/videos/basic_usage.mp4" type="video/mp4">
</video>

Since 2016, Radiance has been used to control many different lights and projectors,
from weddings to burning man.
There's still plenty of improvements to be made,
but the featureset we have now is the culmination of seven years of
parties, output hardware, making mistakes, and rewriting.

![Radiance controlling light strips at a wedding reception]({attach}wedding.jpg)

![Radiance at Burning Man]({attach}mvp.jpg)
