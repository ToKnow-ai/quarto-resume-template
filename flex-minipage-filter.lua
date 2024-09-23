---@param doc pandoc.Pandoc
---@return pandoc.Pandoc
local function flex_minipage_filter(doc)
    local new_block  = doc.blocks:walk {
        ---@param block pandoc.Block
        ---@return pandoc.Block
        Block = function(block)
            if block.attr and block.attr.classes and block.attr.classes:includes("d-flex") then
                block.content:insert(
                    1,
                    pandoc.Div(pandoc.List {
                        pandoc.RawBlock('latex', "\\borderBox {"),
                        pandoc.RawBlock('latex', "\\begingroup"),
                        pandoc.RawBlock('latex', "\\let\\par\\relax"),
                        pandoc.RawBlock('latex', "\\begin{minipage}[t]{0.6\\textwidth}")
                    })
            )
                -- The first block
                block.content:insert(
                    3, 
                    pandoc.Div(pandoc.List {
                        pandoc.RawBlock('latex', "\\end{minipage}"),
                        pandoc.RawBlock('latex', "\\hfill")
                    }))
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
