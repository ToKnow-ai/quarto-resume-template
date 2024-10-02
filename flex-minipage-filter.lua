---@param doc pandoc.Pandoc
---@return pandoc.Pandoc
local function flex_minipage_filter(doc)
    local new_block  = doc.blocks:walk {
        ---@param block pandoc.Block
        ---@return pandoc.Block
        Block = function(block)
            if quarto.doc.is_format("pdf") and block.attr and block.attr.classes and block.attr.classes:includes("d-flex") then
                block.content:insert(1, pandoc.RawBlock('latex', "\\borderBox {"))
                block.content:insert(2, pandoc.RawBlock('latex', "\\begingroup"))
                block.content:insert(3, pandoc.RawBlock('latex', "\\let\\par\\relax"))
                block.content:insert(4, pandoc.RawBlock('latex', "\\begin{minipage}[t]{0.6\\textwidth}"))
                -- The first block
                block.content:insert(6, pandoc.RawBlock('latex', "\\end{minipage}"))
                block.content:insert(7, pandoc.RawBlock('latex', "\\hfill"))
                block.content:insert(pandoc.RawBlock('latex', "\\endgroup"))
                block.content:insert(pandoc.RawBlock('latex', "}"))
            end
            return block
        end
    }
    return pandoc.Pandoc(new_block, doc.meta)
end

return {{
    Pandoc = flex_minipage_filter
}}
