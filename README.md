# quick-development

## Quick nvim setup

- nvim test.py
- `:split autosave.lua`
- `ctrl+w k` to go back to the test.py window
- `:vsplit new`
- `:lua print(vim.api.nvim_get_current_buf())` and get the number (for instance 3)
- Go to test.py window and change something and save using `:w`

This should result in saved test.py on the left and the same file executed and printed the result on the right 'new window'
The idea intially seen/stolen from the [TJ's video](https://www.youtube.com/watch?v=HlfjpstqXwE)

Happy quick developing
