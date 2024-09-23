---@param doc pandoc.Pandoc
---@return pandoc.Pandoc
local function flex_minipage_filter(doc)
    local new_block  = doc.blocks:walk {
        ---@param block pandoc.Block
        ---@return pandoc.Block
        Block = function(block)
            if block.attr and block.attr.classes and block.attr.classes:includes("d-flex") then
                block.content:insert(1, pandoc.RawInline('latex', "\\borderBox {"))
                block.content:insert(2, pandoc.RawInline('latex', "\\begingroup"))
                block.content:insert(3, pandoc.RawInline('latex', "\\let\\par\\relax"))
                block.content:insert(4, pandoc.RawInline('latex', "\\begin{minipage}[t]{0.6\\textwidth}"))
                -- The first block
                block.content:insert(6, pandoc.RawInline('latex', "\\end{minipage}"))
                block.content:insert(7, pandoc.RawInline('latex', "\\hfill"))
                block.content:insert(pandoc.RawInline('latex', "\\endgroup"))
                block.content:insert(pandoc.RawInline('latex', "}"))

                quarto.log.debug('block', block)
            end
            return block
        end
    }
    return pandoc.Pandoc(new_block, doc.meta)
end

return {{
    Pandoc = flex_minipage_filter
}}
