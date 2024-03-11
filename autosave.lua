
local attach_to_buffer = function(current_buf, pattern, command)
  vim.api.nvim_create_autocmd("BufWritePost", {
  group = vim.api.nvim_create_augroup("STNVGroup", { clear = true }),
  pattern = pattern,
  callback = function()
    local append_data = function(_, data)
      if data then
        vim.api.nvim_buf_set_lines(current_buf, -1, -1, false, data)
      end
    end

    vim.api.nvim_buf_set_lines(current_buf, 0, -1, false, {"========= Quick Test ========="})
    vim.fn.jobstart(command, {
      stdout_buffered = true,
      on_stderr = append_data,
      on_stdout = append_data,
    })
  end,
})
end

attach_to_buffer(3, "*.py", {"python3", "my.py"})
