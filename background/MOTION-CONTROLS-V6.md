# Motion Controls v6 — November 4, 2026

The native floating controls use the existing Hairline kernel and unchanged
Glow, Flow, and Saturation drawing functions, with defaults 21/30/69.

The trigger is positioned over an empty, fixed-height anchor. The controls live
in a shadow root in a manual popover in the browser top layer. The anchor is
never modified when opening or closing. No parent, sibling, Squarespace grid,
page padding, scroll position, or document height is written by the component.
No growing iframe is used. Component CSS cannot select unrelated page elements.

The supplied 41.9-second reference recording shows floating items using fade,
16px translation, scale .8, and 60ms stagger. v6 applies those transitions with
`@starting-style` and discrete display transitions. The desktop cards unfold
above the trigger when space permits, otherwise below; mobile retains three
equal columns. Only the cards animate. A closed card uses display:none and inert
content, so it cannot leave a hidden click target.

## Install

Replace the previous controls Code Block with motion-controls-placeholder.html.
Replace only the previous controls Footer Code Injection with
motion-controls-footer.html. Keep unrelated background/carousel code. Do not
install the old slider mount beside v6. Save and reload the page.

## Verification

motion-controls-verification.json records desktop 1440px and touch-mobile 390px
browser checks. Every element outside the overlay was measured on every frame
through four complete open/close cycles. All external rectangles, attributes,
spacing, grid areas, document scroll dimensions, and scroll positions stayed
identical. Separate checks covered transformed/clipped ancestors, closed hit
areas, fonts, keyboard, mouse/touch, reduced motion, and value delivery to the
real background document.

This verifies the supplied installation and browser fixture, not an unseen
Squarespace installation. No claim of inspecting that live installation is made.

Reference: https://developer.chrome.com/blog/what-is-the-top-layer/
Reference: https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using
Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style

Existing hosted v5 and background/carousel files remain unchanged for recovery.
