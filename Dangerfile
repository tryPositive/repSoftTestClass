# Dangerfile

# Check if commit title length exceeds 50 characters
commit_title = git.commit_title
if commit_title.length > 50
  warn("Commit title is too long (maximum 50 characters). Current length: #{commit_title.length}")
end

# Check for an empty line between title and description
commit_message = git.commit_message.split("\n")
if commit_message.size > 1 && commit_message[1] != ""
  warn("There should be an empty line between the commit title and description.")
end

# Check that the description has at least 5 characters
if commit_message.size > 2
  description = commit_message[2..-1].join("\n").strip
  if description.length < 5
    warn("Commit description must be at least 5 characters long.")
  end

  # Check each line of the description for a maximum of 72 characters
  description_lines = description.split("\n")
  description_lines.each do |line|
    if line.length > 72
      warn("Description line exceeds 72 characters: #{line}")
    end
  end
end
