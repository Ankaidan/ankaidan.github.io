function csv2list(filepath)
    local file = io.open(filepath, "r")
    if not file then
        print("Error: Could not open file " .. filepath)
        return nil
    end

    local data = {} -- 二次元リストとなるテーブル

    for line in file:lines() do
        local row = {} -- 各行のデータを格納するテーブル
        -- カンマで文字列を分割
        for field in string.gmatch(line .. "\t", "([^\t]*)\t") do
            table.insert(row, field)
        end
        table.insert(data, row)
    end

    file:close()
    return data
end

--ここからメイン
function nJtoE(num, ans, w1, w2, w3, w4, cor)
    local num_index = 0
    local csv_file = "./files/kamitango.tsv"
    local csv_data = csv2list(csv_file)
    local output = "\\JtoE{"
    for i, row in ipairs(csv_data) do
        if row[1] == num then
            if row[5] == "" then
                output = output .. row[2] .. "}{" .. row[3]
            else
                output = output .. string.gsub(row[5],"\\enword{.*}","\\blank") .. "}{" .. string.gsub(row[6], "\\jpword{([^}]*)}{[^}]*}", "%1", 1)
            end
            output = output.."}{"..w1.."}{"..w2.."}{"..w3.."}{"..w4.."}{"..cor.."}{"
            if ans == cor then
                output = output.."\\correct"
            elseif ans ~= "" then
                output = output.."\\incorrect{\\maru{"..ans.."}}"
            end
            output = output.."}{"..num.."}"
            break
        end
    end
    return(output)
end

function nEW(num, ans, tf, comm)
    local csv_file = "./files/kamitango.tsv"
    local csv_data = csv2list(csv_file)
    local mkd_ans = ans
    local output = "\\EW{"
    for i, row in ipairs(csv_data) do
        if row[1] == num then
            if tf == "T" then
                mkd_ans = "\\correct["..ans.."]"
            elseif tf == "F" then
                mkd_ans = "\\incorrect["..string.match(row[5],"\\enword{([^}]*)}").."]{"..ans.."}"
            elseif tf == "" then
                if row[5] ~= "" then
                    mkd_ans = string.match(row[5],"\\enword{([^}]*)}")
                else 
                    mkd_ans = row[2]
                end
            end
            mkd_ans = mkd_ans.."\\comm{"..comm.."}"
            if row[5] == "" then
                output = output .. row[2] .. "}{" .. row[3].."}{"..mkd_ans.."}{"..num.."}"
            else
                output = output .. string.gsub(row[5],"\\enword{(.).*}","\\blank[%1]") .. "}{" .. string.gsub(row[6], "\\jpword{([^}]*)}{([^}]*)}", "%1%2", 1).."}{"..mkd_ans.."}{"..num.."}"
            end
            break
        end
    end
    return(output)
end

function nEtoJ(num, ans, tf, comm)
    local csv_file = "./files/kamitango.tsv"
    local csv_data = csv2list(csv_file)
    local mkd_ans = ans
    local output = "\\EtoJ{"
    for i, row in ipairs(csv_data) do
        if row[1] == num then
            if tf == "T" then
                mkd_ans = "\\correct["..ans.."]"
            elseif tf == "F" then
                mkd_ans = "\\incorrect["..string.gsub(row[6],".*\\jpword{([^}]*)}{([^}]*)}.*","%1%2",1).."]{"..ans.."}"
            elseif tf == "" then
                mkd_ans = string.gsub(row[6],".*\\jpword{([^}]*)}{([^}]*)}.*","%1%2",1)
            end
            mkd_ans = mkd_ans.."\\comm{"..comm.."}"
            if row[5] == "" then
                output = output .. row[2] .. "}{"..mkd_ans.."}{"..num.."}"
            else
                output = output .. string.gsub(row[5],"\\enword{([^}]*)}","\\underline{%1}",1) .. "}{"..mkd_ans.."}{"..num.."}"
            end
            break
        end
    end
    return(output)
end  





print(nEW("6","ans","","comm"))
-- \EtoJ{<英語例文>}{<正答>}{<番号>}
-- \nEtoJ{<番号>}{<受験者の解答>}{<正誤>}{<コメント>}
-- \EW{<英語例文>}{<和訳>}{<正答>}{<番号>}
-- \nEW{<番号>}{<受験者の解答>}{T/F}%{<コメント>}
-- \JtoE{<英語例文>}{<和訳>}{単語(rand)}{単語(rand)}{単語(rand)}{単語(rand)}{<正答>}{<受験者の解答>}{<番号>}
-- \nJtoE{<番号>}{<受験者の解答>}{単語(rand)}{単語(rand)}{単語(rand)}{単語(rand)}{<正答>}


-- if csv_data then
--     for i, row in ipairs(csv_data) do
--         for j, field in ipairs(row) do
--             io.write(field .. " ")
--         end
--         io.write("\n")
--     end
-- end

