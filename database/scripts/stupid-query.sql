select c.name, s.state from cities c
join states s ON  c.state_id = s.id
where s.state in (
	select state from states
)
order by s.long_name, c.name
