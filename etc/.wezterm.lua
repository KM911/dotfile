-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This will hold the configuration.
local config = wezterm.config_builder()
-- This is where you actually apply your config choices

-- For example, changing the color scheme:
config.color_scheme = "Darcula"

-- set active tab color as #40e0f0
-- config
config.colors = {
	tab_bar = {
		active_tab = {
			bg_color = "#000000",
			fg_color = "#40e0f0",
		},
	},
	-- focus pane color
}

config.inactive_pane_hsb = {

	hue = 0.7,
	saturation = 0.9,
	brightness = 0.4,
}

-- launch nu and execute the default command
config.default_prog = { "/usr/bin/nu", "-e hello" }

-- and finally, return the configuration to wezterm

local act = wezterm.action
-- config.disable_default_key_bindings = true

config.keys = {
	-- Create a new tab in the same domain as the current pane.
	-- This is usually what you want.
	{ key = "t", mods = "CTRL", action = act.SpawnTab("CurrentPaneDomain") },
	{ key = "v", mods = "CMD", action = wezterm.action.SplitVertical({ domain = "CurrentPaneDomain" }) },
	{
		key = "g",
		mods = "CMD",
		action = wezterm.action.SplitPane({
			direction = "Left",
			size = { Percent = 50 },
		}),
	},
	{
		key = "[",
		mods = "CMD",
		action = act.ActivatePaneDirection("Up")
	},
	{
		key = "]",
		mods = "CMD",
		action = act.ActivatePaneDirection("Down")
	},
	{
		key = "'",
		mods = "CMD",
		action = act.ActivatePaneDirection("Right"),
	},
	{
		key = ";",
		mods = "CMD",
		action = act.ActivatePaneDirection("Left"),
	},
	{
		key = 'LeftArrow',
		mods = 'CMD',
		action = act.ActivatePaneDirection('Left'),
	  },
	  {
		key = 'RightArrow',
		mods = 'CMD',
		action = act.ActivatePaneDirection('Right'),
	  },
	  {
		key = 'UpArrow',
		mods = 'CMD',
		action = act.ActivatePaneDirection('Up'),
	  },
	  {
		key = 'DownArrow',
		mods = 'CMD',
		action = act.ActivatePaneDirection('Down'),
	  },
	{
		key = "Tab",
		mods = "CTRL",
		action = act.ActivateTabRelative(1),
	},
	{
		key = "w",
		mods = "CTRL",
		action = act.CloseCurrentTab({ confirm = false }),
	},
	-- save and paster
	-- PasteFrom="Clipboard" CopyTo="Clipboard"
	{ key = "v", mods = "CTRL|SHIFT", action = act.PasteFrom("Clipboard") },
	{ key = "v", mods = "CTRL", action = act.PasteFrom("Clipboard") },
	-- { key = "c", mods = "CTRL", action = act.CopyTo("Clipboard") },
}

for i = 1, 8 do
	-- CTRL+ALT + number to move to that position
	table.insert(config.keys, {
		key = tostring(i),
		mods = "CTRL",
		action = wezterm.action.ActivateTab(i - 1),
	})
end

config.use_ime = true
config.xim_im_name = "fcitx"

-- set font size
config.font_size = 10.0

return config
