# Function to get Pokémon data by ID
get_pokemon_data <- function(id) {
  url <- paste0("https://pokeapi.co/api/v2/pokemon/", id)
  response <- GET(url)
  content(response, as = "parsed", type = "application/json")
}

# Function to get Pokémon species data by ID
get_pokemon_species_data <- function(id) {
  url <- paste0("https://pokeapi.co/api/v2/pokemon-species/", id)
  response <- GET(url)
  content(response, as = "parsed", type = "application/json")
}

# Function to get evolution chain data
get_evolution_chain_data <- function(url) {
  response <- GET(url)
  content(response, as = "parsed", type = "application/json")
}

# Fetch data for the first 10 Pokémon
pokemon_list <- lapply(1:151, get_pokemon_data)
species_list <- lapply(1:151, get_pokemon_species_data)

# Extract relevant data, including sprites, and create a dataframe
extract_data <- function(pokemon, species) {
  stats <- pokemon$stats
  types <- sapply(pokemon$types, function(x) x$type$name)
  abilities <- sapply(pokemon$abilities, function(x) x$ability$name)
  sprites <- pokemon$sprites
  egg_cycles <- species$hatch_counter
  legendary <- species$is_legendary
  mythical <- species$is_mythical
  base_happiness <- species$base_happiness
  evolution_chain_url <- species$evolution_chain$url
  evolution_chain <- get_evolution_chain_data(evolution_chain_url)
  
  data.frame(
    id = pokemon$id,
    name = pokemon$name,
    height = pokemon$height,
    weight = pokemon$weight,
    base_experience = pokemon$base_experience,
    hp = stats[[1]]$base_stat,
    attack = stats[[2]]$base_stat,
    defense = stats[[3]]$base_stat,
    sp_atk = stats[[4]]$base_stat,
    sp_def = stats[[5]]$base_stat,
    speed = stats[[6]]$base_stat,
    types = paste(types, collapse = ", "),
    abilities = paste(abilities, collapse = ", "),
    front_default = sprites$front_default,
    front_shiny = sprites$front_shiny,
    back_default = sprites$back_default,
    back_shiny = sprites$back_shiny,
    egg_cycles = egg_cycles,
    legendary = legendary,
    mythical = mythical,
    base_happiness = base_happiness,
    evolution_chain_url = evolution_chain_url,
    stringsAsFactors = FALSE
  )
}

# Combine Pokémon data with species data
combined_data <- Map(extract_data, pokemon_list, species_list)
pokemon_data <- do.call(rbind, combined_data)
print(pokemon_data)

# Function to create image HTML
image_html <- function(url) {
  return(paste0('<img src="', url, '" height="42">'))
}

# Create the interactive table with reactable and reactablefmtr
reactable(
  pokemon_data,
  columns = list(
    front_default = colDef(name = "Front Default", cell = function(value) {
      image_html(value)
    }, html = TRUE),
    front_shiny = colDef(name = "Front Shiny", cell = function(value) {
      image_html(value)
    }, html = TRUE),
    back_default = colDef(name = "Back Default", cell = function(value) {
      image_html(value)
    }, html = TRUE),
    back_shiny = colDef(name = "Back Shiny", cell = function(value) {
      image_html(value)
    }, html = TRUE),
    id = colDef(name = "#", align = "center"),
    name = colDef(name = "Name"),
    types = colDef(name = "Types"),
    abilities = colDef(name = "Abilities"),
    hp = colDef(name = "HP"),
    attack = colDef(name = "Attack"),
    defense = colDef(name = "Defense"),
    sp_atk = colDef(name = "Sp. Atk"),
    sp_def = colDef(name = "Sp. Def"),
    speed = colDef(name = "Speed"),
    height = colDef(name = "Height"),
    weight = colDef(name = "Weight"),
    base_experience = colDef(name = "Base Experience"),
    egg_cycles = colDef(name = "Egg Cycles"),
    legendary = colDef(name = "Legendary"),
    mythical = colDef(name = "Mythical"),
    base_happiness = colDef(name = "Base Happiness"),
    evolution_chain_url = colDef(name = "Evolution Chain URL")
  ),
  defaultPageSize = 50,
  filterable = TRUE,
  style = list(
    td = list(verticalAlign = "middle")
  )
)






```{r}

# Your existing code to create the table
table <- reactable(
  data,
  columns = list(
    `#` = colDef(name = "#", align = "center", cell = function(value) {
      value
    }),
    Name = colDef(name = "Name"),
    `Type 1` = colDef(name = "Type 1", cell = function(value) {
      type_color(value)
    }, html = TRUE, filterable = TRUE),
    `Type 2` = colDef(name = "Type 2", cell = function(value) {
      type_color(value)
    }, html = TRUE, filterable = TRUE),
    Total = colDef(name = "Total", cell = data_bars(data, 
                                                    text_position = "outside-base", 
                                                    fill_color = c("#e81cff", "#40c9ff"), 
                                                    background = "#e5e5e5", 
                                                    fill_gradient = TRUE, 
                                                    box_shadow = TRUE, 
                                                    round_edges = TRUE
    )),
    HP = colDef(name = "HP", cell = data_bars(data, 
                                              text_position = "outside-base", 
                                              fill_color = c("#e81cff", "#40c9ff"), 
                                              background = "#e5e5e5", 
                                              fill_gradient = TRUE, 
                                              box_shadow = TRUE, 
                                              round_edges = TRUE
    )),
    Attack = colDef(name = "Attack", cell = data_bars(data, 
                                                      text_position = "outside-base", 
                                                      fill_color = c("#e81cff", "#40c9ff"), 
                                                      background = "#e5e5e5", 
                                                      fill_gradient = TRUE, 
                                                      box_shadow = TRUE, 
                                                      round_edges = TRUE
    )),
    Defense = colDef(name = "Defense", cell = data_bars(data, 
                                                        text_position = "outside-base", 
                                                        fill_color = c("#e81cff", "#40c9ff"), 
                                                        background = "#e5e5e5", 
                                                        fill_gradient = TRUE, 
                                                        box_shadow = TRUE, 
                                                        round_edges = TRUE
    )),
    `Sp. Atk` = colDef(name = "Sp. Atk", cell = data_bars(data, 
                                                          text_position = "outside-base", 
                                                          fill_color = c("#e81cff", "#40c9ff"), 
                                                          background = "#e5e5e5", 
                                                          fill_gradient = TRUE, 
                                                          box_shadow = TRUE, 
                                                          round_edges = TRUE
    )),
    `Sp. Def` = colDef(name = "Sp. Def", cell = data_bars(data, 
                                                          text_position = "outside-base", 
                                                          fill_color = c("#e81cff", "#40c9ff"), 
                                                          background = "#e5e5e5", 
                                                          fill_gradient = TRUE, 
                                                          box_shadow = TRUE, 
                                                          round_edges = TRUE
    )),
    Speed = colDef(name = "Speed", cell = data_bars(data, 
                                                    text_position = "outside-base", 
                                                    fill_color = c("#e81cff", "#40c9ff"), 
                                                    background = "#e5e5e5", 
                                                    fill_gradient = TRUE, 
                                                    box_shadow = TRUE, 
                                                    round_edges = TRUE
    )),
    Generation = colDef(name = "Generation", align = "center"),
    Legendary = colDef(name = "Legendary", align = "center", cell = function(value) {
      if (value) {
        return("\u2605")  # Unicode star symbol for legendary
      } else {
        return("")
      }
    })
  ),
  defaultPageSize = 10,
  filterable = TRUE,
  style = list(
    td = list(verticalAlign = "middle")
  )
)

# Save the table as an HTML file
saveWidget(table, "pokemon_table.html")

# Now you can share the "pokemon_table.html" file with your friend

```




# Function to color the cells based on type
type_color <- function(value) {
  if (is.na(value) || value == "NA") {
    return("")
  }
  color <- type_colors[[tolower(value)]]
  if (!is.null(color)) {
    return(paste0('<span style="color: white; background-color: ', color, '; padding: 4px; border-radius: 4px;">', value, '</span>'))
  }
  return(value)
}

# Create the interactive table with reactable and reactablefmtr
reactable(
  data,
  columns = list(
    `#` = colDef(name = "#", align = "center", cell = function(value) {
      value
    }),
    Name = colDef(name = "Name"),
    `Type 1` = colDef(name = "Type 1", cell = function(value) {
      type_color(value)
    }, html = TRUE, filterable = TRUE),
    `Type 2` = colDef(name = "Type 2", cell = function(value) {
      type_color(value)
    }, html = TRUE, filterable = TRUE),
    Total = colDef(name = "Total", cell = data_bars(data, 
                                                    text_position = "outside-base", 
                                                    fill_color = c("#e81cff", "#40c9ff"), 
                                                    background = "#e5e5e5", 
                                                    fill_gradient = TRUE, 
                                                    box_shadow = TRUE, 
                                                    round_edges = TRUE
    )),
    HP = colDef(name = "HP", cell = data_bars(data, 
                                              text_position = "outside-base", 
                                              fill_color = c("#e81cff", "#40c9ff"), 
                                              background = "#e5e5e5", 
                                              fill_gradient = TRUE, 
                                              box_shadow = TRUE, 
                                              round_edges = TRUE
    )),
    Attack = colDef(name = "Attack", cell = data_bars(data, 
                                                      text_position = "outside-base", 
                                                      fill_color = c("#e81cff", "#40c9ff"), 
                                                      background = "#e5e5e5", 
                                                      fill_gradient = TRUE, 
                                                      box_shadow = TRUE, 
                                                      round_edges = TRUE
    )),
    Defense = colDef(name = "Defense", cell = data_bars(data, 
                                                        text_position = "outside-base", 
                                                        fill_color = c("#e81cff", "#40c9ff"), 
                                                        background = "#e5e5e5", 
                                                        fill_gradient = TRUE, 
                                                        box_shadow = TRUE, 
                                                        round_edges = TRUE
    )),
    `Sp. Atk` = colDef(name = "Sp. Atk", cell = data_bars(data, 
                                                          text_position = "outside-base", 
                                                          fill_color = c("#e81cff", "#40c9ff"), 
                                                          background = "#e5e5e5", 
                                                          fill_gradient = TRUE, 
                                                          box_shadow = TRUE, 
                                                          round_edges = TRUE
    )),
    `Sp. Def` = colDef(name = "Sp. Def", cell = data_bars(data, 
                                                          text_position = "outside-base", 
                                                          fill_color = c("#e81cff", "#40c9ff"), 
                                                          background = "#e5e5e5", 
                                                          fill_gradient = TRUE, 
                                                          box_shadow = TRUE, 
                                                          round_edges = TRUE
    )),
    Speed = colDef(name = "Speed", cell = data_bars(data, 
                                                    text_position = "outside-base", 
                                                    fill_color = c("#e81cff", "#40c9ff"), 
                                                    background = "#e5e5e5", 
                                                    fill_gradient = TRUE, 
                                                    box_shadow = TRUE, 
                                                    round_edges = TRUE
    )),
    Generation = colDef(name = "Generation", align = "center"),
    Legendary = colDef(name = "Legendary", align = "center", cell = function(value) {
      if (value) {
        return("\u2605")  # Unicode star symbol for legendary
      } else {
        return("")
      }
    })
  ),
  defaultPageSize = 50,
  filterable = TRUE,  # Enable filtering
  style = list(
    td = list(verticalAlign = "middle")
  )
)

