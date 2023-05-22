# WriteSQLInsertsPy

Add in txt head -

DECLARE @rowCount int = (select count(*) from powerapps.SLAEscalationMatrix)
select @rowCount;
IF (@rowCount = 0)
BEGIN
END
