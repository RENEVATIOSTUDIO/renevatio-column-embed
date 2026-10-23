# Validation — 2026-10-22

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
- Nothing has been published until the user approves the dedicated public repository and Pages deployment.
