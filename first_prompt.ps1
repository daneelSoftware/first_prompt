$PROJECT='first_prompt'

# $Env:OPENAI_API_KEY="..."
# $Env:ANTHROPIC_API_KEY="..."

if ( $Env:OPENAI_API_KEY -eq $null ){
	echo "OPENAI_API_KEY not set"
} else {
	echo "OPENAI_API_KEY set"	
}
if ( $Env:ANTHROPIC_API_KEY -eq $null ){
	echo "ANTHROPIC_API_KEY not set"
} else {
	echo "ANTHROPIC_API_KEY set"	
}
$start=Get-Date -UFormat "%Y/%m/%d %R"
echo "start prompt $PROJECT at : $start"
python -m $PROJECT
$stop=Get-Date -UFormat "%Y/%m/%d %R"
echo "stop prompt $PROJECT at : $stop"