# Validation — 2026-10-22

## Approved motion and readability update

Stephen authorized a 24-second turn, 1.09× hover growth, 9% hover speed, and a subtle readable-backside correction. He then canceled the formation inversion and supplied a new startup screenshot. The existing formation is preserved with a 0.19-radian starting phase fitted to that screenshot. Earlier speed/scale measurements below describe the original release.

- Browser-measured normal angular speed: −0.26179938779915507 rad/s, versus −2π/24 = −0.2617993877991494. This is a 24-second turn in the original direction.
- Focus interaction uses the same slowdown/growth target as pointer hover. Browser diagnostics settled at speed multiplier 0.0900000769931966 and whole-card scale 1.09000.
- All nine textures loaded with no failures; no shader or JavaScript warnings/errors in the final local build.
- Static startup diagnostics report phase 0.19; visual comparison preserves the supplied LevelUp-at-top formation with upright images and corrected readable backside logos.
- Reverse texture coordinates crossfade as a whole image within approximately ±2° of the card center facing edge-on. This avoids a seam traveling across the curved surface.
- The revised maximum hover size is included in the existing envelope fit. The scene was visually checked in 320×650 and 700×500 blocks.
- Initial phase no longer advances while textures load, so the supplied pose is the starting pose after image readiness.
- Existing links, editor pause, reduced motion, rim colors/timing, and Squarespace snippet remain in place. Squarespace itself was not edited.

## Passed locally

- Nine project records in the user's original URL order; all nine textures loaded.
- Automatic build fetched all nine original Squarespace URLs. SHA-256 hashes of downloaded images matched the nine supplied Desktop originals byte-for-byte.
- Every destination is initially `https://www.renevatio.studio/`, with `_top` navigation.
- Normal speed measured in the browser: −0.222019 rad/s; configured value −0.222 rad/s. Full turn from configured speed: 28.3026365 seconds.
- Interaction target speed settled at 0.1800000667 of normal. Stable keyboard-interaction measurement: −0.0398149 rad/s versus the −0.03996 rad/s target (sampling/frame timing explains the small measured difference).
- Pointer hit testing selected the intended visible card, enlarged the whole curved squircle to 1.05×, and revealed the gradient rim.
- The static scene's phase remained at zero while hover enlargement remained available.
- The entire iframe matched the resizable test block at 392×765, 320×650, and 700×500. The 3D envelope includes maximum hover growth when fitting the scene.
- A simulated Squarespace `.sqs-edit-mode-active` parent hid the live iframe, showed the static iframe, and set static-frame pointer events to none.
- Card click attempted same-tab top-level navigation to the requested temporary destination. The preview browser reported DNS resolution failure for that destination; the requested link was retained.
- JavaScript module syntax, Python build syntax, image manifest order/count, source/copy hashes, and link values passed checks.
- No new rendering/shader/image errors were reported after switching to same-origin image copies.

## Limits of these checks

- Squarespace's actual editor, actual plan's iframe acceptance, existing page CSS, and existing z-index hierarchy have not been changed or tested. Those require inserting the final snippet in the user's selected block.
- Narrow **widget** dimensions were tested. The browser's viewport override did not take effect, so this is not a certified physical-phone test.
- Reduced-motion behavior follows `prefers-reduced-motion`; its static rendering and hover paths were exercised through the local static mode. The user's operating-system accessibility setting was not changed.
- The dedicated public repository and Pages deployment were explicitly approved and are now published. Squarespace itself remains unmodified.

## Published verification

- GitHub Pages action 39882821680 succeeded after Pages was enabled.
- Live URL: https://renevatiostudio.github.io/renevatio-column-embed/ .
- The live browser reported `ready=true`, `count=9`, no failed textures, all nine requested `_top` links, and no console warnings/errors.
- The final Squarespace snippet uses this actual hosting URL for the live and static editor frames.
